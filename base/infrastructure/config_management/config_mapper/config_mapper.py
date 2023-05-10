# -*- coding: utf-8 -*-


import configparser
import re

# Domain
from base.domain.config_management.config_mapper import BaseConfigMapper


class ConfigMapper(BaseConfigMapper):
    """
    ConfigMapper
    """

    def __init__(self, config_parser, custom_sections: list = None, custom_options: list = None):
        """
        ConfigMapper constructor
        @param config_parser: config_parser
        @type config_parser: config_parser
        @param custom_sections: custom_sections
        @type custom_sections: list
        @param custom_options: custom_options
        @type custom_options: list
        """

        if type(config_parser) != configparser.ConfigParser:
            raise ValueError(f"Error config_parser: {config_parser} is not {configparser.ConfigParser}")

        if not isinstance(custom_sections, (list, type(None))):
            raise ValueError(f"Error custom_sections: {custom_sections} is not list type")

        if not isinstance(custom_options, (list, type(None))):
            raise ValueError(f"Error custom_options: {custom_options} is not list type")

        self.__config_parser = config_parser
        self.__custom_sections = custom_sections
        self.__custom_options = custom_options

    def map_config_data(self):
        """
        map_config_data
        @return: config_data
        @rtype: dict
        """

        config_data = {}

        for section, option in self.__config_parser.items():

            if section in self.__custom_sections:

                config_data[section] = {}

                for config, parameter in option.items():

                    is_list_format = True if re.match('[, \n]', parameter) else False
                    is_custom_options = True if config in self.__custom_options else False
                    is_list = is_list_format or is_custom_options

                    parameter_items = [item for item in re.split('[, \n]', parameter) if item != ''] if is_list else parameter

                    config_data[section][config] = parameter_items

        return config_data
