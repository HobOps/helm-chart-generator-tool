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

        deployment_resources = deepcopy(conf["common-library"]["Deployment"])

        for component in deployment_resources:

            component_env_vars: list = deployment_resources["common-library"]["Deployment"][component]["env"]
            counter = 0

            for env in component_env_vars:
                search_env = re.search(self.__config_data, env["value"])

                if not search_env:
                    conf["common-library"]["Deployment"][component]["env"].pop(counter)

                counter += 1

        return conf
