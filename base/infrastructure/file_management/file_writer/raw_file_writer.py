# coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.common.value_objects import ListValueObject
from base.domain.file_management.file_constants import file_mode_values
from base.domain.file_management.file_constants import file_type_values
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.path_management.path_handler import BasePathHandler


class RawFileWriter(BaseFileWriter):
    """
    RawFileWriter
    """

    def __init__(self, path_handler: BasePathHandler = None, file_handler: BaseFileHandler = None):
        """
        RawFileWriter constructor
        """

        if not isinstance(path_handler, (BasePathHandler, type(None))):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        self.__path_handler = path_handler or PathHandler(target_path='/')

        if not self.__path_handler.stored_path.exists():
            raise ValueError(f"Error stored_path: {self.__path_handler.stored_path} doesn't exists in file system")

        if self.__path_handler.stored_path.suffix != file_type_values.raw:
            raise ValueError(f"Error path_handler: {path_handler} file_type_suffix is not dot(.)")

        self.__file_handler = file_handler or FileHandler(
            file_mode=file_mode_values.write,
            path_handler=self.__path_handler,
        )

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

        with self.__file_handler as raw_file_handler:
            raw_file_handler.writelines('\n'.join(data_value.value))

