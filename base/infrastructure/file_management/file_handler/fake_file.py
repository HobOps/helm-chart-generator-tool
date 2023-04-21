# -*- coding: utf-8 -*-


from typing import List


# Domain
from base.domain.file_management.file_handler import BaseFile


class FakeFile(BaseFile):
    """
    FakeFile
    """

    def __init__(self, initial_content: str = None):
        """
        BaseFile constructor
        """

        if not isinstance(initial_content, (str, type(None))):
            raise ValueError(f"Error initial_content: {initial_content} is not str type")

        self.__file_open = False
        self.__file_content: str = initial_content

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

    def writelines(self, data_to_write: List[str]):
        """
        writelines
        """

        if not isinstance(data_to_write, list):
            raise ValueError(f"Error data_to_write: {data_to_write} is not list type")

        if not self.__file_open:
            raise ValueError(f"Error file is not open")

        data_to_write_in_lines = ""

        for line in data_to_write:
            data_to_write_in_lines += f"{line}\n"

        self.__file_content = data_to_write_in_lines

    def close(self):
        """
        read
        """

        self.__file_open = False

    @property
    def content(self):
        """
        content
        @return: content
        @rtype: str
        """

        return self.__file_content
