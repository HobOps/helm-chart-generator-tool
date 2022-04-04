import yaml
import argparse
from kubernetes import client, config
from kubernetes.client import V1ConfigMapEnvSource, V1ContainerPort, V1EnvFromSource, V1EnvVarSource, V1SecretEnvSource


def write_file(path, values, mode='yaml'):
    import os
    # Create directory
    directory = os.path.dirname(path)
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)

    # Write file
    if mode == 'yaml':
        with open(path, 'w') as outfile:
            yaml.dump(values, outfile, default_flow_style=False, sort_keys=False)
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
            result[section]['context'] = chart_config['kubernetes']['context']
            result[section]['namespace'] = chart_config['kubernetes']['namespace']
        elif section == 'chart':
            result[section]['appVersion'] = chart_config['chart']['appVersion']
            result[section]['name'] = chart_config['chart']['name']
            result[section]['description'] = chart_config['chart']['description']
            result[section]['type'] = chart_config['chart']['type']
            result[section]['version'] = chart_config['chart']['version']
            result[section]['appVersion'] = chart_config['chart']['appVersion']
            result[section]['maintainers'] = parse_config_list(chart_config['chart']['maintainers'])
            result[section]['sources'] = parse_config_list(chart_config['chart']['sources'])
            result[section]['baselineVersion'] = chart_config['chart']['baselineVersion']
            result[section]['baselineName'] = chart_config['chart']['baselineName']
            result[section]['baselineRepository'] = chart_config['chart']['baselineRepository']
        elif section == 'components':

            for kind in chart_config['components']:
                result[section][convert_values(kind)] = list()
                result[section][convert_values(kind)] = parse_config_list(chart_config['components'][kind])
        else:
            result.pop(section)
    return result


def parse_config_list(config_list):
    import re
    result = list()
    # for item in re.split(',| |\n', config_list):
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
        if kind == 'ConfigMap':
            for component in conf['components'][kind]:
                values[component] = create_configmap(component)
                pass
        elif kind == 'Secret':
            for component in conf['components'][kind]:
                values[component] = create_secret(component)
                pass
        elif kind in ['Deployment', 'StatefulSet']:
            for component in conf['components'][kind]:
                values[component] = create_workload(
                    kind=kind,
                    name=component,
                    k8s_client=client,
                    namespace=conf['kubernetes']['namespace']
                )
                pass
        elif kind == 'Ingress':
            for component in conf['components'][kind]:
                values[component] = create_ingress(
                    name=component,
                    k8s_client=client,
                    namespace=conf['kubernetes']['namespace']
                )
                pass
        conf['kubernetes']['values'][kind] = values
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
    write_file(f"charts/{conf['chart']['name']}/.helmignore", data, mode='raw')
    pass


def create_chart_file(conf):
    # Render Chart maintainers
    maintainers = list()
    for item in conf['chart']['maintainers']:
        maintainers.append(dict(name=item))
    conf['chart']['maintainers'] = maintainers

    # Render dependencies
    dependencies = list()
    for kind in conf['components']:
        for dependency in conf['components'][kind]:
            dependencies.append(dict(
                alias=dependency,
                name=conf['chart']['baselineName'],
                version=conf['chart']['baselineVersion'],
                repository=conf['chart']['baselineRepository'],
            ))
    conf['chart']['dependencies'] = dependencies

    # Remove unnecessary keys from dictionary
    for item in ['baselineVersion', 'baselineName', 'baselineRepository']:
        conf['chart'].pop(item)

    write_file(f"charts/{conf['chart']['name']}/Chart.yaml", conf['chart'])
    pass


def create_values_file(conf):
    write_file(f"charts/{conf['chart']['name']}/values.yaml", remove_empty_from_dict(conf['kubernetes']['values']))
    pass


def create_helm_chart(conf):
    create_helmignore_file(conf)
    create_chart_file(conf)
    create_values_file(conf)
    pass


def create_environment_values_file(conf):
    file = f"environments/{conf['chart']['name']}/{conf['chart']['name']}.values.yaml.gotmpl"
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
                data.append(f"  replicas: {conf['kubernetes']['values'][kind][component]['replicas']}")
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
        ingress='Ingress'
    )
    return values[value]


def to_dict(item):
    if type(item) in [
        V1ConfigMapEnvSource,
        V1ContainerPort,
        V1EnvFromSource,
        V1EnvVarSource,
        V1SecretEnvSource
    ]:
        return item.to_dict()
    else:
        return None


def remove_empty_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d


def read_env(items):
    variables_to_remove = [
        'STAKATER_OCP_CONFIG_CONFIGMAP',
    ]
    env = list()
    if type(items) is list:
        for item in items:
            if item.name in variables_to_remove:
                break
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


def read_annotations(annotations: dict):
    result = annotations
    annotations_to_remove = [
        'deployment.kubernetes.io/revision',
        'field.cattle.io/publicEndpoints',
        'meta.helm.sh/release-name',
        'meta.helm.sh/release-namespace',
        'objectset.rio.cattle.io/applied',
        'objectset.rio.cattle.io/id',
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
    if tls is list:
        for item in tls:
            result.append(dict(
                secretName=item.secret_name,
                hosts=item.hosts
            ))
    return result


def create_configmap(name):
    print(name)
    return dict(
        kind='ConfigMap',
        fullnameOverride=name,
        data={}
    )


def create_secret(name):
    print(name)
    return dict(
        kind='Secret',
        fullnameOverride=name,
        stringData={}
    )


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
        )
    )


def create_workload(kind, name, k8s_client, namespace):
    v1 = k8s_client.AppsV1Api()
    result = dict(kind=kind)
    print(name)
    ret = ''
    if kind == "StatefulSet":
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


def create_ingress(name: str, k8s_client, namespace):
    ingress_name = name.replace('-ingress', '')
    v1 = k8s_client.NetworkingV1Api()
    ret = v1.list_namespaced_ingress(
        field_selector="metadata.name={name}".format(name=ingress_name),
        namespace=namespace
    )
    print(ingress_name)
    return dict(
        kind='Ingress',
        fullnameOverride=ingress_name,
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

    # Creates helm chart files
    create_helm_chart(config_settings)
    create_environment_values_file(config_settings)


if __name__ == '__main__':
    main()
