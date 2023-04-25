# -*- coding: utf-8 -*-


from typing import List


# Infrastructure
from base.infrastructure.file_management.file_validator import FileTypeValidator

# Domain
from base.domain.file_management.file_handler import BaseFile


class FakeFile(BaseFile):
    """
    FakeFile
    """

    def __init__(self, file_name: str = None, file_type_suffix: str = None, initial_content: str = None):
        """
        BaseFile constructor
        """

        if not isinstance(file_name, (str, type(None))):
            raise ValueError(f"Error file_name: {file_name} is not str type")

        if not isinstance(file_type_suffix, (str, type(None))):
            raise ValueError(f"Error file_type_suffix: {file_type_suffix} is not str type")

        if not isinstance(initial_content, (str, type(None))):
            raise ValueError(f"Error initial_content: {initial_content} is not str type")

        self.__file_name: str = file_name
        self.__file_type_suffix: str = file_type_suffix
        self.__file_content: str = initial_content
        self.__file_open = False

    def open(self):
        """
        open
        @return: None
        @rtype: None
        """

        self.__file_open = True

    def read(self):
        """
        read
        """

        if not self.__file_open:
            raise ValueError(f"Error file is not open")

        return self.__file_content

    def write(self, data_to_write: str):
        """
        write
        """

        if not isinstance(data_to_write, str):
            raise ValueError(f"Error data_to_write: {data_to_write} is not str type")

        if not self.__file_open:
            raise ValueError(f"Error file is not open")

        self.__file_content = f"{self.__file_content}{data_to_write}"

    def writelines(self, data_to_write: str):
        """
        writelines
        """

        if not isinstance(data_to_write, str):
            raise ValueError(f"Error data_to_write: {data_to_write} is not str type")

        if not self.__file_open:
            raise ValueError(f"Error file is not open")

        self.__file_content = data_to_write

    def close(self):
        """
        read
        """

        self.__file_open = False

    @property
    def name(self):
        """
        name
        @return: file_name
        @rtype: str
        """

        return self.__file_name + self.__file_type_suffix

    @property
    def suffix(self):
        """
        suffix
        @return: suffix
        @rtype: str
        """

        return self.__file_type_suffix

    @property
    def content(self):
        """
        content
        @return: content
        @rtype: str
        """

        return self.__file_content

