# -*- coding: utf-8 -*-


from settings import Settings


# Global variable
app_version = "version21"


def write_file_version21(path, values, mode='yaml'):
    """
    write_file_version21
    """

    from app.v1.modules.file_manager import ScriptFileWriterManager

    root_path = Settings.get_root_path().as_posix()
    path = f"{root_path}/{path}"

    ScriptFileWriterManager.write_file(path=path, values=values, mode=mode)


def write_file_version22(path, values, mode='yaml'):
    """
    write_file_version22
    """

    from app.v2.modules.file_manager import AppFileWriterManager

    root_path = Settings.get_root_path().as_posix()
    path = f"/{path}"

    file_writer = AppFileWriterManager(root_path=root_path)
    file_writer.write_file(path=path, values=values, mode=mode)


def write_file(path, values, mode='yaml'):
    """
    write_file
    """

    global app_version

    if app_version == "version21":
        write_file_version21(path=path, values=values, mode=mode)

    if app_version == "version22":
        write_file_version22(path=path, values=values, mode=mode)


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

    from app.v2.modules.config_manager import AppConfigManager

    root_path = Settings.get_root_path().as_posix()

    config_manager = AppConfigManager(root_path=root_path)
    config_data = config_manager.parse_config(component_name=component_name)

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

    if app_version == "version21":
        config_data = parse_config_version1(component_name=component_name)

    if app_version == "version22":
        config_data = parse_config_version21(component_name=component_name)

    return config_data


def load_kubernetes_config_version1(config_settings):
    """
    load_kubernetes_config_version1
    """

    from app.v1.modules.kubernetes_manager import ScriptKubernetesConfigLoader

    ScriptKubernetesConfigLoader.load_kubernetes_config(config_settings=config_settings)


def load_kubernetes_config(config_settings):
    """
    load_kubernetes_config
    """

    global app_version

    if app_version == "version21":
        load_kubernetes_config_version1(config_settings)

    if app_version == "version22":
        load_kubernetes_config_version1(config_settings)


def load_kubernetes_data_version1(config_settings):
    """
    load_kubernetes_data_version1
    """

    from app.v1.modules.kubernetes_manager import ScriptKubernetesDataLoader

    ScriptKubernetesDataLoader.load_kubernetes_data(config_settings)


def load_kubernetes_data(config_settings):
    """
    load_kubernetes_data
    """

    global app_version

    if app_version == "version21":
        load_kubernetes_data_version1(config_settings=config_settings)

    if app_version == "version22":
        load_kubernetes_data_version1(config_settings=config_settings)


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

    if app_version == "version21":
        create_vars_file_version1(config_settings)

    if app_version == "version22":
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

    if app_version == "version21":
        create_helmignore_file_version1(conf)

    if app_version == "version22":
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

    if app_version == "version21":
        create_chart_file_version1(conf)

    if app_version == "version22":
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

    if app_version == "version21":
        create_values_file_version1(conf)

    if app_version == "version22":
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

    if app_version == "version21":
        create_environment_values_file_version1(config_settings)

    if app_version == "version22":
        create_environment_values_file_version1(config_settings)


class AppMainManagerV22:
    """
    AppMainManagerV22
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
        app_version = f"version{args.version}"

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
