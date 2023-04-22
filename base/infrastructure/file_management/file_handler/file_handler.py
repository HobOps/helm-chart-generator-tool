# -*- coding: utf-8 -*-


from unittest.mock import Mock


# Domain
from base.domain.file_management.file_handler import BaseFile
from base.domain.file_management.file_handler import BaseFileHandler


class FileHandler(BaseFileHandler):

    def __init__(self, file_mode: str = 'r', file_path: str = None, file_obj: BaseFile = None):
        """
        FileHandler constructor
        """

        if not isinstance(file_mode, (str, type(None))):
            raise ValueError(f"Error file_mode: {file_mode} is not a str type")

        if not isinstance(file_path, (str, type(None))):
            raise ValueError(f"Error file_path: {file_path} is not a str type")

        if not isinstance(file_obj, (BaseFile, type(None))):
            raise ValueError(f"Error file_obj: {file_obj} is not a {BaseFile} type")

        self.file = file_obj or open(file_path, file_mode)

    def __enter__(self):
        """
        __enter__
        @return: None
        @rtype: None
        """

        if self.file is None:
            raise ValueError(f"Error file: {self.file} is None")

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        __exit__
        @param exc_type: exc_type
        @type exc_type: str
        @param exc_val: exc_val
        @type exc_val: str
        @param exc_tb: exc_tb
        @type exc_tb: str
        @return: None
        @rtype: None
        """

        self.file.close()
