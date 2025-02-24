# -*- coding: utf-8 -*-


import configparser


# Infrastructure
from framework.base.infrastructure.file_management.file_handler import FileHandler


# Domain
from framework.base.domain.config_management.config_reader import BaseConfigReader
from framework.base.domain.file_management.file_constants.file_mode_values import file_mode_values
from framework.base.domain.file_management.file_handler import BaseFileHandler
from framework.base.domain.path_management.path_doubles import BasePath


class ConfigReader(BaseConfigReader):
    """
    ConfigReader
    """

    def __init__(self, path_obj: BasePath, file_handler: BaseFileHandler = None, config_data: dict = None):
        """
        ConfigReader constructor
        @param path_obj: path_obj
        @type path_obj: BasePath
        @param file_handler: file_handler
        @type file_handler: BaseFileHandler
        @param config_data: config_data
        @type config_data: dict
        """

        if not isinstance(path_obj, BasePath):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        if not isinstance(config_data, (dict, type(None))):
            raise ValueError(f"Error config_data: {config_data} is not dict type")

        if not path_obj.exists():
            raise ValueError(f"Error path_obj: {path_obj} doesn't exists in the file system")

        if not path_obj.is_file():
            raise ValueError(f"Error path_obj: {path_obj} is not a file path")

        self.__stored_path = path_obj
        self.__config_data = config_data
        self.__config_parser = configparser.ConfigParser()
        self.__config_parser.optionxform = str
        self.__file_handler = file_handler or FileHandler(file_mode=file_mode_values.read, path_obj=path_obj)

    def get_config_parser(self):
        """
        get_config_parser
        @return: config_parser
        @rtype: configparser.ConfigParser
        """

        if self.__config_data:
            self.__config_parser.read_dict(self.__config_data)

        if not self.__config_data:
            with self.__file_handler as file_handler:
                self.__config_parser.read_file(file_handler)

        return self.__config_parser

