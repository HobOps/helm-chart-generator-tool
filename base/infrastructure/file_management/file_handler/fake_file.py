# -*- coding: utf-8 -*-


# Domain
from base.domain.file_management.file_handler import BaseFile


class FakeFile(BaseFile):
    """
    FakeFile
    """

    def __init__(self):
        """
        BaseFile constructor
        """

        self.__file_open = True
        self.__file_content = ""

    def read(self):
        """
        read
        """

        if not self.__file_open:
            raise ValueError(f"Error file is not open")

        return self.__file_content

    def write(self, data_to_write: str):
        """
        read
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

