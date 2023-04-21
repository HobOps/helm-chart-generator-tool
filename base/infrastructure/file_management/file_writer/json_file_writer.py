# coding: utf-8 -*-


import json


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler

# Domain
from base.domain.common.value_objects import DictValueObject
from base.domain.file_management.file_constants import file_mode_values
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.path_management.path_handler import BasePathHandler


class JsonFileWriter(BaseFileWriter):
    """
    JsonFileWriter
    """

    def __init__(self, path_handler: BasePathHandler):
        """
        JsonFileWriter constructor
        """

        if not isinstance(path_handler, BasePathHandler):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        self.__path_handler = path_handler

    def write_file(self, data: dict):
        """
        write_file
        @param data: data
        @type data: dict
        @return: None
        @rtype: None
        """

        data_value = DictValueObject(data)

        with FileHandler(file_path=self.__path_handler.target_path.__str__(), file_mode=file_mode_values.write) as json_file_handler:
            json.dump(data_value.value, json_file_handler, sort_keys=False, indent=4)

