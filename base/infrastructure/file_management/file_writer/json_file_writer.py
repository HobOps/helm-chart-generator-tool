# coding: utf-8 -*-


import json


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler

# Domain
from base.domain.common.value_objects import DictValueObject
from base.domain.file_management.file_constants import file_mode_values
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.path_management.path_doubles import BasePath


class JsonFileWriter(BaseFileWriter):
    """
    JsonFileWriter
    """

    def __init__(self, path_obj: BasePath, file_handler: BaseFileHandler = None):
        """
        JsonFileWriter constructor
        """

        if not isinstance(path_obj, BasePath):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        self.__path_obj = path_obj
        self.__file_handler = file_handler or FileHandler(path_obj=self.__path_obj, file_mode=file_mode_values.write)

    def write_file(self, data: dict):
        """
        write_file
        @param data: data
        @type data: dict
        @return: None
        @rtype: None
        """

        if not isinstance(data, dict):
            raise ValueError(f"Error data: {data} is not dict type")

        data_value = DictValueObject(data)

        with self.__file_handler as json_file_handler:
            json.dump(data_value.value, json_file_handler, sort_keys=False, indent=4)
