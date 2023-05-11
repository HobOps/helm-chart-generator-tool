# -*- coding: utf-8 -*-


import configparser
import re

# Domain
from base.domain.config_management.config_mapper import BaseConfigMapper


class ConfigMapper(BaseConfigMapper):
    """
    ConfigMapper
    """

    def __init__(self, config_parser, filter_sections: list = None):
        """
        ConfigMapper constructor
        @param config_parser: config_parser
        @type config_parser: config_parser
        @param filter_sections: custom_sections
        @type filter_sections: list
        """

        if type(config_parser) != configparser.ConfigParser:
            raise ValueError(f"Error config_parser: {config_parser} is not {configparser.ConfigParser}")

        if not isinstance(filter_sections, (list, type(None))):
            raise ValueError(f"Error filter_sections: {filter_sections} is not list type")

        self.__config_parser = config_parser
        self.__filter_sections = filter_sections

    def map_config_data(self):
        """
        map_config_data
        @return: config_data
        @rtype: dict
        """

        config_data = {}

        for section, option in self.__config_parser.items():

            if section not in self.__filter_sections:

                config_data[section] = {}

                for config, parameter in option.items():

                    is_list_format = True if re.match('[, \n]', parameter) else False
                    parameter_items = [item for item in re.split('[, \n]', parameter) if item != ''] if is_list_format else parameter

                    config_data[section][config] = parameter_items

        return config_data
