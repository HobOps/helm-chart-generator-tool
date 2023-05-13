# -*- coding: utf-8 -*-


import os
from settings import Settings

from kubernetes import client
from kubernetes import config

# Refactor Imports
from app.v1.modules.kubernetes_services import ScriptAnnotationsReaderService
from app.v1.modules.kubernetes_services import ScriptEnvironReaderService
from app.v1.modules.kubernetes_services import ScriptEnvironReaderFromService
from app.v1.modules.kubernetes_services import ScriptHostAliasesReaderService
from app.v1.modules.kubernetes_services import ScriptImagePullSecretsReaderService
from app.v1.modules.kubernetes_services import ScriptIngressRulesReaderService
from app.v1.modules.kubernetes_services import ScriptIngressTlsReaderService
from app.v1.modules.kubernetes_services import ScriptServicesCreatorService
from app.v1.modules.kubernetes_services import ScriptToDictParserService
from app.v1.modules.kubernetes_services import ScriptVolumesReaderService
from app.v1.modules.kubernetes_services import ScriptVolumeMountsReaderService

# Global variable
app_version = "version1"


def write_file_version1(path, values, mode='yaml'):
    """
    write_file_version1
    """

    from app.v1.modules.file_manager import ScriptFileWriterManager

    root_path = Settings.get_root_path().as_posix()
    path = f"{root_path}/{path}"

    ScriptFileWriterManager.write_file(path=path, values=values, mode=mode)


def write_file_version21(path, values, mode='yaml'):
    """
    write_file_version2
    """

    from base.infrastructure.file_management.file_creator import FileWriterCreator
    from base.infrastructure.path_management.path_factory import SimplePathCreator

    root_path = Settings.get_root_path().as_posix()
    target_path = f"/{path}"

    file_path_creator = SimplePathCreator(root_path=root_path)
    file_path = file_path_creator.generate_path(target_path=target_path)

    file_writer_creator = FileWriterCreator(path_obj=file_path)
    file_writer = file_writer_creator.create_file_writer(file_type=mode)
    file_writer.write_file(data=values)


def write_file(path, values, mode='yaml'):
    """
    write_file
    """

    global app_version

    if app_version == "version1":
        write_file_version1(path=path, values=values, mode=mode)

    if app_version == "version21":
        write_file_version21(path=path, values=values, mode=mode)


def parse_config_version1(component_name):
    """
    parse_config_version1
    @param component_name: component_name
    @type component_name: str
    @return: result
    @rtype: dict
    """

    from app.v1.modules.config_manager import ScriptConfigParser

    result = ScriptConfigParser.parse_config(component_name=component_name)

    return result


def parse_config_version21(component_name):
    """
    parse_config_version2
    @param component_name: component_name
    @type component_name: str
    @return: result
    @rtype: dict
    """

    from base.infrastructure.config_management.config_mapper import ConfigMapper
    from base.infrastructure.config_management.config_reader import ConfigReader
    from base.infrastructure.path_management.path_factory import SimplePathCreator

    root_path = Settings.get_root_path().as_posix()
    target_path = f"/config_files/input/configurations/{component_name}.ini"

    path_creator = SimplePathCreator(root_path=root_path)
    created_target_path = path_creator.generate_path(target_path=target_path)

    filter_sections = [
        'DEFAULT',
    ]

    config_reader = ConfigReader(path_obj=created_target_path)
    config_parser = config_reader.get_config_parser()
    config_mapper = ConfigMapper(
        config_parser=config_parser,
        filter_sections=filter_sections,
    )
    config_data = config_mapper.map_config_data()

    return config_data


def parse_config(component_name):
    """
    parse_config
    @param component_name: component_name
    @type component_name: str
    @return: result
    @rtype: dict
    """

    global app_version

    config_data = ""

    if app_version == "version1":
        config_data = parse_config_version1(component_name=component_name)

    if app_version == "version21":
        config_data = parse_config_version21(component_name=component_name)

    return config_data


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


def create_workload_template(ret, name):
    return dict(
        annotations=ScriptAnnotationsReaderService.read_annotations(ret.items[0].metadata.annotations),
        selectorLabels=dict(
            app=name
        ),
        image=dict(
            repository=ret.items[0].spec.template.spec.containers[0].image.split(':')[0],
            tag=ret.items[0].spec.template.spec.containers[0].image.split(':')[1]
        ),
        command=ret.items[0].spec.template.spec.containers[0].command,
        args=ret.items[0].spec.template.spec.containers[0].args,
        env=ScriptEnvironReaderService.read_env(ret.items[0].spec.template.spec.containers[0].env),
        envFrom=ScriptEnvironReaderFromService.read_env_from(ret.items[0].spec.template.spec.containers[0].env_from),
        service=dict(
            ports=ScriptServicesCreatorService.create_services(ret.items[0].spec.template.spec.containers[0].ports)
        ),
        volumes=ScriptVolumesReaderService.read_volumes(ret.items[0].spec.template.spec.volumes),
        volumeMounts=ScriptVolumeMountsReaderService.read_volume_mounts(ret.items[0].spec.template.spec.containers[0].volume_mounts),
        serviceAccount=(ret.items[0].spec.template.spec.service_account, None)[
            ret.items[0].spec.template.spec.service_account == 'default'
        ],
        imagePullSecrets=ScriptImagePullSecretsReaderService.read_image_pull_secrets(ret.items[0].spec.template.spec.image_pull_secrets),
        hostAliases=ScriptHostAliasesReaderService.read_host_aliases(ret.items[0].spec.template.spec.host_aliases),
        readinessProbe=ScriptToDictParserService.to_dict(ret.items[0].spec.template.spec.containers[0].readiness_probe),
        livenessProbe=ScriptToDictParserService.to_dict(ret.items[0].spec.template.spec.containers[0].liveness_probe),
        # TODO: Add missing resources
        # securityContext=to_dict(ret.items[0].spec.template.spec.containers[0].security_context),
        # strategy
        # resources
        # security_context
    )


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
        annotations=ScriptAnnotationsReaderService.read_annotations(ret.items[0].metadata.annotations),
        rules=ScriptIngressRulesReaderService.read_ingress_rules(ret.items[0].spec.rules),
        tls=ScriptIngressTlsReaderService.read_ingress_tls(ret.items[0].spec.tls)
    )


def create_vars_file_version1(conf):
    """
    create_vars_file_version1
    """

    from app.v1.modules.kubernetes_manager import ScriptVarsFileCreator

    ScriptVarsFileCreator.create_vars_file(conf)


def create_vars_file(config_settings):
    """
    create_vars_file
    """

    global app_version

    if app_version == "version1":
        create_vars_file_version1(config_settings)

    if app_version == "version21":
        create_vars_file_version1(config_settings)


def create_helmignore_file_version1(conf):
    """
    create_helmignore_file_version1
    """

    from app.v1.modules.helm_manager import ScriptHelmIgnoreCreator

    ScriptHelmIgnoreCreator.create_helmignore_file(conf)


def create_helmignore_file(conf):
    """
    create_helmignore_file
    """

    global app_version

    if app_version == "version1":
        create_helmignore_file_version1(conf)

    if app_version == "version21":
        create_helmignore_file_version1(conf)


def create_chart_file_version1(conf):
    """
    create_chart_file_version1
    """

    from app.v1.modules.helm_manager import ScriptHelmChartCreator

    ScriptHelmChartCreator.create_chart_file(conf)


def create_chart_file(conf):
    """
    create_chart_file
    """

    global app_version

    if app_version == "version1":
        create_chart_file_version1(conf)

    if app_version == "version21":
        create_chart_file_version1(conf)


def create_values_file_version1(conf):
    """
    create_values_file_version1
    """

    from app.v1.modules.helm_manager import ScriptHelmValuesCreator

    ScriptHelmValuesCreator.create_values_file(conf)


def create_values_file(conf):
    """
    create_values_file
    """

    global app_version

    if app_version == "version1":
        create_values_file_version1(conf)

    if app_version == "version21":
        create_values_file_version1(conf)


def create_helm_chart(config_settings):
    create_helmignore_file(config_settings)
    create_chart_file(config_settings)
    create_values_file(config_settings)
    pass


def create_environment_values_file_version1(conf):
    """
    create_environment_values_file_version1
    """

    from app.v1.modules.kubernetes_manager import ScriptEnvironValuesFileCreator

    ScriptEnvironValuesFileCreator.create_environment_values_file(conf)


def create_environment_values_file(config_settings):
    """
    create_environment_values_file
    """

    global app_version

    if app_version == "version1":
        create_environment_values_file_version1(config_settings)

    if app_version == "version21":
        create_environment_values_file_version1(config_settings)


class AppMainManager:
    """
    AppMainManager
    """

    @staticmethod
    def run(args):
        """
        run
        @param args: args
        @type args: args
        @return: None
        @rtype: None
        """

        global app_version
        app_version = args.version

        # Loads configuration
        config_settings = parse_config(args.name)
        load_kubernetes_config(config_settings)
        load_kubernetes_data(config_settings)

        # Create env vars in JSON file
        create_vars_file(config_settings)

        # Creates helm chart files
        create_helm_chart(config_settings)
        create_environment_values_file(config_settings)
