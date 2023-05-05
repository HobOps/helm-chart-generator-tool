# -*- coding: utf-8 -*-


import configparser
import re

# Domain
from base.domain.config_management.config_mapper import BaseConfigMapper


class ConfigMapper(BaseConfigMapper):
    """
    ConfigMapper
    """

    @staticmethod
    def map_config_data(config_parser):
        """
        map_config_data
        @param config_parser: config_parser
        @type config_parser: configparser
        @return: config_data
        @rtype: dict
        """

        if type(config_parser) != configparser.ConfigParser:
            raise ValueError(f"Error config_parser: {config_parser} is not {configparser.ConfigParser}")

        list_parser = lambda parameter: [item for item in re.split('[, \n]', parameter) if item != '']
        filter_to_list = lambda parameter: list_parser(parameter) if re.match('[, \n]', parameter) else parameter

        config_data = {
            section: {
                config: filter_to_list(parameter) for config, parameter in option.items()
            } for section, option in config_parser.items()
        }

        return config_data
