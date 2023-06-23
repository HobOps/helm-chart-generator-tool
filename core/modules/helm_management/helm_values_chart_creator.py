# -*- coding: utf-8 -*-


# Domain
from core.modules.helm_management import HelmConfigValuesFilter
from core.modules.helm_management import HelmDeployEnvVarsFilter
from core.modules.helm_management import HelmValuesDataProcessing


class HelmValuesChartCreator:
    """
    HelmValuesChartCreator
    """

    @staticmethod
    def create_values_file(conf: dict):
        """
        create_values_file
        @param conf: conf 
        @type conf: dict
        @return: conf
        @rtype: dict
        """""

        if not isinstance(conf, dict):
            raise ValueError(f"Error conf: {conf} is not dict type")

        pattern = r'\$\(.*?\)'

        values_filter = HelmConfigValuesFilter()
        deploy_envs_filter = HelmDeployEnvVarsFilter(config_data=pattern)

        helm_values_pipeline = HelmValuesDataProcessing().add_handler(values_filter).add_handler(deploy_envs_filter)
        output_data = helm_values_pipeline.execute(input_data=conf)

        return output_data
    