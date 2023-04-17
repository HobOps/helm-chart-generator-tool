import argparse
import os
from kubernetes import client, config


def write_file(path, values, mode='yaml'):
    import os
    import yaml
    import json
    # Create directory
    directory = os.path.dirname(path)
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)

    # Write file
    if mode == 'yaml':
        yaml.add_representer(str, str_presenter)
        yaml.representer.SafeRepresenter.add_representer(str, str_presenter)
        with open(path, 'w') as outfile:
            yaml.dump(values, outfile, default_flow_style=False, sort_keys=False)
    elif mode == 'json':
        with open(path, 'w') as outfile:
            json.dump(values, outfile, sort_keys=False, indent=4)
    else:
        with open(path, 'w') as outfile:
            outfile.writelines('\n'.join(values))
    pass


def parse_config(component_name):
    # Open config file
    import configparser
    import os.path
    config_path = f'configurations/{component_name}.ini'
    chart_config = configparser.ConfigParser()
    if os.path.isfile(config_path):
        chart_config.read(config_path)
    else:
        print(f'The configuration file {config_path} does not exist.')
        exit(1)

    # Parse config file
    result = dict()
    for section in chart_config:
        result[section] = dict()
        if section == 'kubernetes':
            result[section]['context'] = chart_config[section]['context']
            result[section]['namespace'] = chart_config[section]['namespace']
        elif section == 'flags':
            result[section]['remove_ingress_suffix'] = chart_config[section]['remove_ingress_suffix']
        elif section == 'chart':
            result[section]['apiVersion'] = chart_config[section]['apiVersion']
            result[section]['name'] = chart_config[section]['name']
            result[section]['description'] = chart_config[section]['description']
            result[section]['type'] = chart_config[section]['type']
            result[section]['version'] = chart_config[section]['version']
            result[section]['appVersion'] = chart_config[section]['appVersion']
            result[section]['maintainers'] = parse_config_list(chart_config[section]['maintainers'])
            result[section]['sources'] = parse_config_list(chart_config[section]['sources'])
            result[section]['baseChartVersion'] = chart_config[section]['baseChartVersion']
            result[section]['baseChartName'] = chart_config[section]['baseChartName']
            result[section]['baseChartRepository'] = chart_config[section]['baseChartRepository']
        elif section == 'components':
            for kind in chart_config[section]:
                result[section][convert_values(kind)] = list()
                result[section][convert_values(kind)] = parse_config_list(chart_config[section][kind])
        else:
            result.pop(section)
    return result


def parse_config_list(config_list):
    import re
    result = list()
    for item in re.split('[, \n]', config_list):
        if item != '':
            result.append(item)
    return result


def load_kubernetes_config(config_settings):
    contexts, active_context = config.list_kube_config_contexts()
    if not contexts:
        print("Cannot find any context in kube-config file.")
        exit(1)
    return config.load_kube_config(context=config_settings['kubernetes']['context'])


def load_kubernetes_data(conf):
    conf['kubernetes']['values'] = dict()
    for kind in conf['components'].keys():
        print("==== " + kind)
        values = dict()
        if kind in ['ConfigMap', 'Secret']:
            for component in conf['components'][kind]:
                values[component] = create_configmap_or_secret(
                    kind=kind,
                    name=component,
                    k8s_client=client,
                    namespace=conf['kubernetes']['namespace']
                )
                pass
        elif kind in ['Job', 'Deployment', 'StatefulSet']:
            for component in conf['components'][kind]:
                values[component] = create_workload(
                    kind=kind,
                    name=component,
                    k8s_client=client,
                    namespace=conf['kubernetes']['namespace']
                )
                pass
        elif kind == 'Ingress':
            try:
                name_suffix = conf['flags']['remove_ingress_suffix']
            except KeyError:
                name_suffix = ''
            for component in conf['components'][kind]:
                values[component] = create_ingress(
                    name=component,
                    name_suffix=name_suffix,
                    k8s_client=client,
                    namespace=conf['kubernetes']['namespace'],
                )
                pass
        conf['kubernetes']['values'][kind] = values
    pass


def create_vars_file(conf):
    field = dict(
        ConfigMap='data',
        Secret='stringData'
    )
    for kind in conf['kubernetes']['values']:
        if kind in ['ConfigMap', 'Secret']:
            for item in conf['kubernetes']['values'][kind]:
                write_file(
                    f"output/vars/{conf['chart']['name']}/{item}.json",
                    remove_empty_from_dict(conf['kubernetes']['values'][kind][item][field[kind]]),
                    mode='json'
                )
    pass


def create_helmignore_file(conf):
    data = [
        '# Patterns to ignore when building packages.',
        '# This supports shell glob matching, relative path matching, and',
        '# negation (prefixed with !). Only one pattern per line.',
        '.DS_Store',
        '# Common VCS dirs',
        '.git/',
        '.gitignore',
        '.bzr/',
        '.bzrignore',
        '.hg/',
        '.hgignore',
        '.svn/',
        '# Common backup files',
        '*.swp',
        '*.bak',
        '*.tmp',
        '*.orig',
        '*~',
        '# Various IDEs',
        '.project',
        '.idea/',
        '*.tmproj',
        '.vscode/',
        ''
    ]
    write_file(f"output/charts/{conf['chart']['name']}/.helmignore", data, mode='raw')
    pass


def create_chart_file(conf):
    # Render Chart maintainers
    maintainers = list()
    for item in conf['chart']['maintainers']:
        maintainers.append(dict(name=item))
    conf['chart']['maintainers'] = maintainers

    # Render dependencies
    conf['chart']['dependencies'] = [dict(
        name=conf['chart']['baseChartName'],
        version=conf['chart']['baseChartVersion'],
        repository=conf['chart']['baseChartRepository'],
    )]
    # Remove unnecessary keys from dictionary
    for item in ['baseChartVersion', 'baseChartName', 'baseChartRepository']:
        conf['chart'].pop(item)
    write_file(f"output/charts/{conf['chart']['name']}/Chart.yaml", conf['chart'])
    pass


def create_values_file(conf):
    values = dict()
    values['common-library'] = dict()
    for kind in conf['kubernetes']['values']:
        values['common-library'][kind] = dict()
        for item in conf['kubernetes']['values'][kind]:
            values['common-library'][kind][item] = conf['kubernetes']['values'][kind][item]
            # Remove variables from "values.yaml" file
            # if kind == 'ConfigMap':
            #     values['common-library'][kind][item]['data'] = {}
            # elif kind == 'Secret':
            #     values['common-library'][kind][item]['data'] = {}
            #     values['common-library'][kind][item]['stringData'] = {}
    write_file(f"output/charts/{conf['chart']['name']}/values.yaml", remove_empty_from_dict(values))
    pass


def create_helm_chart(conf):
    create_helmignore_file(conf)
    create_chart_file(conf)
    create_values_file(conf)
    pass


def create_environment_values_file(conf):
    file = f"output/environments/{conf['chart']['name']}/{conf['chart']['name']}.values.yaml.gotmpl"
    data = list()
    data.append('# Load global and environment settings')
    data.append('{{ readFile "../../include/values.global.yaml" }}')
    data.append('{{ readFile "values.environment.yaml" }}')
    data.append('')
    for kind in conf['kubernetes']['values'].keys():
        if kind == 'ConfigMap':
            data.append(f'### {kind}')
            for component in conf['kubernetes']['values'][kind]:
                data.append(f'{component}:')
                data.append(f'  data: {{}}')
                # Save variables to file
                data.append(f'')
                pass
        elif kind == 'Secret':
            data.append(f'### {kind}')
            for component in conf['kubernetes']['values'][kind]:
                data.append(f'{component}:')
                data.append(f'  stringData: {{}}')
                data.append(f'')
                pass
        elif kind in ['Deployment', 'StatefulSet']:
            data.append(f'### {kind}')
            for component in conf['kubernetes']['values'][kind]:
                data.append(f'{component}:')
                data.append(f'  <<: *default-environment')
                data.append(f'  <<: *default-global-resources-nolimit')
                data.append(f"  replicaCount: {conf['kubernetes']['values'][kind][component]['replicas']}")
                data.append(f"  image:")
                data.append(f"    repository: {conf['kubernetes']['values'][kind][component]['image']['repository']}")
                data.append(f"    tag: {conf['kubernetes']['values'][kind][component]['image']['tag']}")
                data.append(f'')
                pass
        elif kind == 'Ingress':
            data.append(f'### {kind}')
            for component in conf['kubernetes']['values'][kind]:
                data.append(f'{component}:')
                if conf['kubernetes']['values'][kind][component]['annotations']:
                    data.append(f'  annotations:')
                    for key, value in conf['kubernetes']['values'][kind][component]['annotations'].items():
                        data.append(f"    {key}: {value}")
                data.append(f"  host: {conf['kubernetes']['values'][kind][component]['rules'][0]['host']}")
                pass
            data.append('')
    write_file(file, data, mode='raw')
    pass


def create_services(services):
    result = list()
    if type(services) is list:
        for service in services:
            result.append(dict(
                name=service.name,
                port=service.container_port,
                hostIp=service.host_ip,
                hostPort=service.host_port,
                protocol=service.protocol
            ))
    return result


def convert_values(value):
    values = dict(
        configmap='ConfigMap',
        secret='Secret',
        deployment='Deployment',
        statefulset='StatefulSet',
        ingress='Ingress',
        job='Job'
    )
    return values[value]


def to_dict(item):
    if type(item) in [
        client.V1ConfigMapEnvSource,
        client.V1ContainerPort,
        client.V1EnvFromSource,
        client.V1EnvVarSource,
        client.V1SecretEnvSource,
        client.V1ConfigMapVolumeSource,
        client.V1SecretVolumeSource,
        client.V1VolumeMount,
        client.V1Probe
    ]:
        # This section converts dictionary keys from underscore to camel case
        values = item.to_dict()
        if type(item) is client.V1EnvVarSource:
            values['configMapKeyRef'] = values.pop('config_map_key_ref')
        elif type(item) is client.V1ConfigMapVolumeSource:
            values['defaultMode'] = values.pop('default_mode')
        elif type(item) is client.V1SecretVolumeSource:
            values['defaultMode'] = values.pop('default_mode')
            values['secretName'] = values.pop('secret_name')
        elif type(item) is client.V1Probe:
            values['failureThreshold'] = values.pop('failure_threshold')
            values['httpGet'] = values.pop('http_get')
            values['initialDelaySeconds'] = values.pop('initial_delay_seconds')
            values['periodSeconds'] = values.pop('period_seconds')
            values['successThreshold'] = values.pop('success_threshold')
            values['tcpSocket'] = values.pop('tcp_socket')
            values['terminationGracePeriodSeconds'] = values.pop('termination_grace_period_seconds')
            values['timeoutSeconds'] = values.pop('timeout_seconds')
        else:
            values = item.to_dict()
        return values
    else:
        return None


def remove_empty_from_dict(d):
    """efficient way to remove keys with empty strings from a dict
    Ref: https://stackoverflow.com/questions/12118695/efficient-way-to-remove-keys-with-empty-strings-from-a-dict"""
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d


def str_presenter(dumper, data):
    """configures yaml for dumping multiline strings
    Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data"""
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


def read_env(items):
    variables_to_remove = [
        'FOO'
    ]
    # TODO: Refactor this section
    prefixes_to_remove = [
        'STAKATER_',
    ]
    env = list()
    if type(items) is list:
        for item in items:
            # Remove variables based on prefixes_to_remove
            if os.path.commonprefix([prefixes_to_remove[0], item.name]) == prefixes_to_remove[0]:
                continue
            elif item.name in variables_to_remove:
                continue
            env.append(dict(
                name=item.name,
                value=item.value,
                valueFrom=to_dict(item.value_from)
            ))
    return env


def read_env_from(items):
    env_from = list()
    if type(items) is list:
        for item in items:
            env_from.append(dict(
                configMapRef=to_dict(item.config_map_ref),
                secretRef=to_dict(item.secret_ref),
                prefix=item.prefix
            ))
    return env_from


def read_volumes(items):
    values = list()
    if type(items) is list:
        for item in items:
            values.append(dict(
                name=item.name,
                configMap=to_dict(item.config_map),
                secret=to_dict(item.secret),
                hostPath=to_dict(item.host_path)
            ))
    return values


def read_volume_mounts(items):
    values = list()
    if type(items) is list:
        for item in items:
            values.append(dict(
                mountPath=item.mount_path,
                mountPropagation=item.mount_propagation,
                name=item.name,
                readOnly=item.read_only,
                subPath=item.sub_path,
                subPathExpr=item.sub_path_expr
            ))
    return values


def read_annotations(annotations: dict):
    result = annotations
    annotations_to_remove = [
        'deployment.kubernetes.io/revision',
        'field.cattle.io/publicEndpoints',
        'meta.helm.sh/release-name',
        'meta.helm.sh/release-namespace',
        'objectset.rio.cattle.io/applied',
        'objectset.rio.cattle.io/id',
        'kubectl.kubernetes.io/last-applied-configuration',
        'kubernetes.io/change-cause',
    ]
    for item in annotations_to_remove:
        result.pop(item, None)
    return result


def read_ingress_rules(rules):
    result = list()
    for item in rules:
        rule = dict()
        rule['host'] = item.host
        rule['http'] = dict(
            paths=list()
        )
        for path in item.http.paths:
            rule['http']['paths'].append(dict(
                path=path.path,
                backend=path.backend.to_dict(),
                pathType=path.path_type
            ))
        result.append(rule)
    return result


def read_ingress_tls(tls):
    result = list()
    if type(tls) is list:
        for item in tls:
            result.append(dict(
                secretName=item.secret_name,
                hosts=item.hosts
            ))
    return result


def read_image_pull_secrets(image_pull_secrets):
    result = list()
    if type(image_pull_secrets) is list:
        for item in image_pull_secrets:
            result.append(dict(
                name=item.name
            ))
    return result


def read_host_aliases(host_aliases):
    result = list()
    if type(host_aliases) is list:
        for item in host_aliases:
            result.append(dict(
                ip=item.ip,
                hostnames=item.hostnames,
            ))
    return result


def create_configmap_or_secret(kind, name, k8s_client, namespace):
    import base64
    v1 = k8s_client.CoreV1Api()
    result = dict()
    print(name)
    ret = ''
    if kind == "ConfigMap":
        ret = v1.list_namespaced_config_map(
            field_selector="metadata.name={name}".format(name=name),
            namespace=namespace,
        )
        result['data'] = ret.items[0].data
    elif kind == "Secret":
        ret = v1.list_namespaced_secret(
            field_selector="metadata.name={name}".format(name=name),
            namespace=namespace,
        )
        string_data = dict()
        for item in ret.items[0].data:
            string_data[item] = base64.b64decode(ret.items[0].data[item]).decode("utf-8")
        result['stringData'] = string_data
    return result


def create_workload_template(ret, name):
    return dict(
        annotations=read_annotations(ret.items[0].metadata.annotations),
        selectorLabels=dict(
            app=name
        ),
        image=dict(
            repository=ret.items[0].spec.template.spec.containers[0].image.split(':')[0],
            tag=ret.items[0].spec.template.spec.containers[0].image.split(':')[1]
        ),
        command=ret.items[0].spec.template.spec.containers[0].command,
        args=ret.items[0].spec.template.spec.containers[0].args,
        env=read_env(ret.items[0].spec.template.spec.containers[0].env),
        envFrom=read_env_from(ret.items[0].spec.template.spec.containers[0].env_from),
        service=dict(
            ports=create_services(ret.items[0].spec.template.spec.containers[0].ports)
        ),
        volumes=read_volumes(ret.items[0].spec.template.spec.volumes),
        volumeMounts=read_volume_mounts(ret.items[0].spec.template.spec.containers[0].volume_mounts),
        serviceAccount=(ret.items[0].spec.template.spec.service_account, None)[
            ret.items[0].spec.template.spec.service_account == 'default'
        ],
        imagePullSecrets=read_image_pull_secrets(ret.items[0].spec.template.spec.image_pull_secrets),
        hostAliases=read_host_aliases(ret.items[0].spec.template.spec.host_aliases),
        readinessProbe=to_dict(ret.items[0].spec.template.spec.containers[0].readiness_probe),
        livenessProbe=to_dict(ret.items[0].spec.template.spec.containers[0].liveness_probe),
        # TODO: Add missing resources
        # securityContext=to_dict(ret.items[0].spec.template.spec.containers[0].security_context),
        # strategy
        # resources
        # security_context
    )


def create_workload(kind, name, k8s_client, namespace):
    v1 = k8s_client.AppsV1Api()
    result = dict()
    print(name)
    ret = ''
    if kind == "Job":
        v1 = k8s_client.BatchV1Api()
        ret = v1.list_namespaced_job(
            field_selector="metadata.name={name}".format(name=name),
            namespace=namespace
        )
    elif kind == "StatefulSet":
        ret = v1.list_namespaced_stateful_set(
            field_selector="metadata.name={name}".format(name=name),
            namespace=namespace
        )
        result = result | dict(replicas=ret.items[0].spec.replicas)
    elif kind == "Deployment":
        ret = v1.list_namespaced_deployment(
            field_selector="metadata.name={name}".format(name=name),
            namespace=namespace
        )
        result = result | dict(replicas=ret.items[0].spec.replicas)
    return result | create_workload_template(ret, name)


def create_ingress(name: str, k8s_client, namespace, name_suffix=''):
    ingress_name = name.replace(name_suffix, '')
    v1 = k8s_client.NetworkingV1Api()
    ret = v1.list_namespaced_ingress(
        field_selector="metadata.name={name}".format(name=ingress_name),
        namespace=namespace
    )
    print(ingress_name)
    return dict(
        annotations=read_annotations(ret.items[0].metadata.annotations),
        rules=read_ingress_rules(ret.items[0].spec.rules),
        tls=read_ingress_tls(ret.items[0].spec.tls)
    )


def main():
    # Parses program arguments
    parser = argparse.ArgumentParser(description='Generates a helm charts from components on a kubernetes cluster.')
    parser.add_argument('--name', action='store', type=str, help="Name of the helm chart")
    args = parser.parse_args()

    # Loads configuration
    config_settings = parse_config(args.name)
    load_kubernetes_config(config_settings)
    load_kubernetes_data(config_settings)

    # Create env vars in JSON file
    create_vars_file(config_settings)

    # Creates helm chart files
    create_helm_chart(config_settings)
    create_environment_values_file(config_settings)


if __name__ == '__main__':
    main()
