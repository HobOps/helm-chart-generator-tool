# -*- coding: utf-8 -*-


# Domain
from base.domain.file_management.file_doubles import BaseFile
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.path_management.path_doubles import BasePath


class FileHandler(BaseFileHandler):

    def __init__(self, file_mode: str = 'r', path_obj: BasePath = None, file_obj: BaseFile = None):
        """
        FileHandler constructor
        """

        if not isinstance(file_mode, (str, type(None))):
            raise ValueError(f"Error file_mode: {file_mode} is not a str type")

        if not isinstance(path_obj, (BasePath, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not a {BasePath} type")

        if not isinstance(file_obj, (BaseFile, type(None))):
            raise ValueError(f"Error file_obj: {file_obj} is not a {BaseFile} type")

        self.__path_obj = path_obj

        self.file = file_obj or open(self.__path_obj.as_posix(), file_mode)

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
