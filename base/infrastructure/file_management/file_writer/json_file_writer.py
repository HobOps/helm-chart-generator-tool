# coding: utf-8 -*-


import json


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.common.value_objects import DictValueObject
from base.domain.file_management.file_constants import file_mode_values
from base.domain.file_management.file_constants import file_type_values
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.path_management.path_handler import BasePathHandler


class JsonFileWriter(BaseFileWriter):
    """
    JsonFileWriter
    """

    def __init__(self, path_handler: BasePathHandler = None, file_handler: BaseFileHandler = None):
        """
        JsonFileWriter constructor
        """

        if not isinstance(path_handler, (BasePathHandler, type(None))):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        self.__path_handler = path_handler or PathHandler(target_path='/')

        if not self.__path_handler.stored_path.exists():
            raise ValueError(f"Error stored_path: {self.__path_handler.stored_path} doesn't exists in file system")

        if self.__path_handler.stored_path.suffix != file_type_values.json:
            raise ValueError(f"Error path_handler: {path_handler} file_type_suffix is not .json")

        self.__file_handler = file_handler or FileHandler(
            file_path=self.__path_handler.stored_path.__str__(),
            file_mode=file_mode_values.write,
        )

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
