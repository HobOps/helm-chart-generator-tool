# -*- coding: utf-8 -*-


from base.domain.config_management.config_doubles import BaseConfig


class ConfigFaker(BaseConfig):
    """
    ConfigFaker
    """

    def __init__(self, config_data: dict = None):
        """
        ConfigFaker
        """

        if not isinstance(config_data, (dict, type(None))):
            raise ValueError(f"Error config_data: {config_data} is not dict type")

        self.__config_data = config_data

    def read(self):
        """
        read
        @return: config_data
        @rtype: dict
        """

        return self.__config_data

