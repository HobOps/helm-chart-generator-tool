# coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler

# Domain
from base.domain.common.value_objects import ListValueObject
from base.domain.file_management.file_constants.file_mode_values import file_mode_values
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.path_management.path_doubles import BasePath


class TextFileWriter(BaseFileWriter):
    """
    TextFileWriter
    """

    def __init__(self, path_obj: BasePath, file_handler: BaseFileHandler = None):
        """
        TextFileWriter constructor
        """

        if not isinstance(path_obj, BasePath):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        if not path_obj.exists():
            raise ValueError(f"Error path_obj: {path_obj} doesn't exists in file system")

        if not path_obj.suffix == file_type_values.text:
            raise ValueError(f"Error path_obj.suffix: {path_obj.suffix} it's not text type")

        self.__path_obj = path_obj
        self.__file_handler = file_handler or FileHandler(path_obj=self.__path_obj, file_mode=file_mode_values.write)

    def write_file(self, data: list):
        """
        write_file
        @param data: data
        @type data: list
        @return: None
        @rtype: None
        """

        if not isinstance(data, list):
            raise ValueError(f"Error data: {data} is not list type")

        data_value = ListValueObject(data)

        with self.__file_handler as text_file_handler:
            text_file_handler.writelines('\n'.join(data_value.value))

