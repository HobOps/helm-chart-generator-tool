# -*- coding: utf-8 -*-


from settings import Settings


# Application
from app.app_management import AppManagerBase
from app.app_management import ArgumentData


def write_file(path, values, mode='yaml'):
    """
    write_file
    """

    from core.modules.file_management import AppFileWriterManager

    root_path = Settings.get_root_path().as_posix()
    path = f"/{path}"

    file_writer = AppFileWriterManager(root_path=root_path)
    file_writer.write_file(path=path, values=values, mode=mode)


def parse_config(component_name):
    """
    parse_config
    @param component_name: component_name
    @type component_name: str
    @return: result
    @rtype: dict
    """

    from core.modules.config_management import AppConfigManager

    root_path = Settings.get_root_path().as_posix()

    config_manager = AppConfigManager(root_path=root_path)
    config_data = config_manager.parse_config(component_name=component_name)

    return config_data


def load_kubernetes_config(config_settings):
    """
    load_kubernetes_config
    """

    from app.v1.modules.kubernetes_manager import ScriptKubernetesConfigLoader

    ScriptKubernetesConfigLoader.load_kubernetes_config(config_settings=config_settings)


def load_kubernetes_data(config_settings):
    """
    load_kubernetes_data
    """

    from app.v1.modules.kubernetes_manager import ScriptKubernetesDataLoader

    ScriptKubernetesDataLoader.load_kubernetes_data(conf=config_settings)


def create_vars_file(config_settings):
    """
    create_vars_file
    """

    from app.v1.modules.kubernetes_manager import ScriptVarsFileCreator

    ScriptVarsFileCreator.create_vars_file(conf=config_settings)

    from core.modules.helm_management.helm_vars_management import HelmDeploymentVarsCreator

    helm_deployment_vars_creator = HelmDeploymentVarsCreator()
    helm_deployment_vars = helm_deployment_vars_creator.create_vars_data(conf=config_settings)

    if helm_deployment_vars:
        path = f"config_files/output/vars/{config_settings['chart']['name']}/deployment_vars.json"
        write_file(path=path, values=helm_deployment_vars, mode="json")


def create_helmignore_file(config_settings):
    """
    create_helmignore_file
    """

    from app.v1.modules.helm_manager import ScriptHelmIgnoreCreator

    ScriptHelmIgnoreCreator.create_helmignore_file(conf=config_settings)


def create_chart_file(config_settings):
    """
    create_chart_file
    """

    from app.v1.modules.helm_manager import ScriptHelmChartCreator

    ScriptHelmChartCreator.create_chart_file(conf=config_settings)


def create_values_file(config_settings):
    """
    create_values_file
    """

    from core.modules.helm_management.helm_values_chart_management import HelmValuesChartCreator

    helm_values_file_path = f"config_files/output/charts/{config_settings['chart']['name']}/values.yaml"

    helm_values_chart_creator = HelmValuesChartCreator()
    helm_values = helm_values_chart_creator.create_values_file(conf=config_settings)

    write_file(path=helm_values_file_path, values=helm_values, mode='yaml')


def create_helm_chart(config_settings):
    create_helmignore_file(config_settings=config_settings)
    create_chart_file(config_settings=config_settings)
    create_values_file(config_settings=config_settings)


def create_environment_values_file(config_settings):
    """
    create_environment_values_file
    """

    from app.v1.modules.kubernetes_manager import ScriptEnvironValuesFileCreator

    ScriptEnvironValuesFileCreator.create_environment_values_file(conf=config_settings)


class AppMainManagerV23(AppManagerBase):
    """
    AppMainManagerV23
    """

    @staticmethod
    def run(args: ArgumentData):
        """
        run
        @param args: args
        @type args: ArgumentData
        @return: version
        @rtype: str
        """

        # Print version
        print(f"Working Version {args.version}")

        # Loads configuration
        config_settings = parse_config(args.name)
        load_kubernetes_config(config_settings)
        load_kubernetes_data(config_settings)

        # Create env vars in JSON file
        create_vars_file(config_settings)

        # Creates helm chart files
        create_helm_chart(config_settings)
        create_environment_values_file(config_settings)

        return "23"
