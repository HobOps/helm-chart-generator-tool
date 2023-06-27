# -*- coding: utf-8 -*-


# Domain
from core.modules.helm_management.helm_values_chart import HelmConfigValuesFilter
from core.modules.helm_management.helm_values_chart import HelmDeployEnvVarsFilter
from core.modules.helm_management.helm_values_chart import HelmStatefulSetEnvVarsFilter
from core.modules.helm_management.helm_values_chart import HelmValuesDataProcessing
from core.modules.utility_services import DictCleanerDataUtility


class HelmValuesChartCreator:
    """
    HelmValuesChartCreator
    """

    DEFAULT_ENV_VAR_PATTERN = r'\$\(.*?\)'

    def __init__(self, config_data: str = None):
        """
        HelmValuesChartCreator constructor
        """

        if not isinstance(config_data, (str, type(None))):
            raise ValueError(f"Error config_data: {config_data} is not str type")

        env_var_pattern = config_data or self.DEFAULT_ENV_VAR_PATTERN

        self.__helm_values_filter = HelmConfigValuesFilter()
        self.__remove_empty_from_dict = DictCleanerDataUtility()
        self.__deployment_env_var_filter = HelmDeployEnvVarsFilter(config_data=env_var_pattern)
        self.__statefulset_env_var_filter = HelmStatefulSetEnvVarsFilter(config_data=env_var_pattern)

    def create_values_file(self, conf: dict):
        """
        create_values_file
        @param conf: conf 
        @type conf: dict
        @return: conf
        @rtype: dict
        """""

        if not isinstance(conf, dict):
            raise ValueError(f"Error conf: {conf} is not dict type")

        helm_values_pipeline = (
            HelmValuesDataProcessing()
            .add_handler(self.__remove_empty_from_dict)
            .add_handler(self.__helm_values_filter)
            .add_handler(self.__deployment_env_var_filter)
            .add_handler(self.__statefulset_env_var_filter)
        )
        output_data = helm_values_pipeline.execute(input_data=conf)

        return output_data
