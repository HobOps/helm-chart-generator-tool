# -*- coding: utf-8 -*-


# Domain
from core.modules.data_management import BaseDataHandler


class HelmDeploymentEnvVarsFilter(BaseDataHandler):
    """
    HelmDeploymentEnvVarsFilter
    """

    def __init__(self, config_data: str = None):
        """
        HelmDeploymentEnvVarsFilter constructor
        @param config_data: config_data
        @type config_data: str
        """

        if not isinstance(config_data, (str, type(None))):
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

        deployment_resources = conf["common-library"].get("Deployment")
        deployment_env_vars = {}

        for component in deployment_resources:
            deployment_env_vars[component] = {"env": deployment_resources[component].get("env")}

        return deployment_env_vars
