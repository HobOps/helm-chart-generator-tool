# coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.common.value_objects import ListValueObject
from base.domain.file_management.file_constants import file_mode_values
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.path_management.path_handler import BasePathHandler


class TextFileWriter(BaseFileWriter):
    """
    TextFileWriter
    """

    def __init__(self, path_handler: BasePathHandler = None, file_handler: BaseFileHandler = None):
        """
        TextFileWriter constructor
        """

        if not isinstance(path_handler, BasePathHandler):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        if not isinstance(file_handler, BaseFileHandler):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        self.__path_handler = path_handler or PathHandler(root_path='/')
        self.__file_handler = file_handler or FileHandler(file_path=self.__path_handler.target_path, file_mode=file_mode_values.write)

    def write_file(self, data: list):
        """
        write_file
        @param data: data
        @type data: list
        @return: None
        @rtype: None
        """

        data_value = ListValueObject(data)

        with self.__file_handler as text_file_handler:
            text_file_handler.writelines('\n'.join(data_value.value))

