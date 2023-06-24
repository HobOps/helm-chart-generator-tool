# -*- coding: utf-8 -*-


import re
from copy import deepcopy

# Domain
from core.modules.data_management import BaseDataHandler


class HelmDeployEnvVarsFilter(BaseDataHandler):
    """
    HelmDeployEnvVarsFilter
    """

    def __init__(self, config_data: str):
        """
        HelmDeployEnvVarsFilter constructor
        @param config_data: config_data
        @type config_data: str
        """

        if not isinstance(config_data, str):
            raise ValueError(f"Error config_data: {config_data} is not str type")

        self.__config_data = config_data

    def process(self, conf: dict):
        """
        process
        @param conf: conf
        @type conf: dict
        @return: conf
        @rtype: dict
        """

        if not isinstance(conf, dict):
            raise ValueError(f"Error conf: {conf} is not dict type")

        deployment_resources = conf["common-library"]["Deployment"]

        for component in deployment_resources:

            component_env_vars: list = deployment_resources[component]["env"]
            filtered_env_ars = [item for item in component_env_vars if re.search(self.__config_data, item['value'])]
            deployment_resources[component]["env"] = filtered_env_ars

        return deployment_resources
