# -*- coding: utf-8 -*-


import configparser


# Domain
from base.domain.config_management.config_reader import BaseConfigReader
from base.domain.path_management.path_doubles import BasePath


class ConfigReader(BaseConfigReader):
    """
    ConfigReader
    """

    def __init__(self, path_obj: BasePath, config_obj=None):
        """
        ConfigReader
        @param path_obj: path_obj
        @type path_obj: BasePath
        """

        if not isinstance(path_obj, BasePath):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not path_obj.exists():
            raise ValueError(f"Error path_obj: {path_obj} doesn't exists in the file system")

        if not path_obj.is_file():
            raise ValueError(f"Error path_obj: {path_obj} is not a file path")

        self.__stored_path = path_obj
        self.__config_parser = config_obj or configparser.ConfigParser()

    def read_config_file(self):
        """
        read_config_file
        @return: config_data
        @rtype: dict
        """

        with self.__config_parser as config_parser:
            config_data = config_parser.read(self.__stored_path.as_posix())

        return config_data



