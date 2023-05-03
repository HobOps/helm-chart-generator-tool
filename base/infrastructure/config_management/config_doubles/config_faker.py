# -*- coding: utf-8 -*-


# Domain
from base.domain.config_management.config_doubles import BaseConfig
from base.domain.file_management.file_doubles import BaseFile


class ConfigFaker(BaseConfig):
    """
    ConfigFaker
    """

    def __init__(self, config_data: dict = None, file_obj: BaseFile = None):
        """
        ConfigFaker
        @param config_data: config_data
        @type config_data: dict
        @param file_obj: file_obj
        @type file_obj: BaseFile
        """

        if not isinstance(config_data, (dict, type(None))):
            raise ValueError(f"Error config_data: {config_data} is not dict type")

        if not isinstance(file_obj, (BaseFile, type(None))):
            raise ValueError(f"Error file_obj: {file_obj} is not an instance of {BaseFile}")

        self.__config_data = config_data
        self.__file_obj = file_obj

    def read(self, target_path: str = None):
        """
        read
        @return: config_data
        @rtype: dict
        """

        if not isinstance(target_path, (str, type(None))):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        return self.__config_data

    def read_file(self):
        """
        read_file
        @return: config_data
        @rtype: dict
        """

        data = self.__file_obj.read()

        return dict(data)

