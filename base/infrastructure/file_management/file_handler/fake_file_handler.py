# -*- coding: utf-8 -*-


from unittest.mock import Mock

from base.domain.file_management.file_handler import BaseFileHandler


class FakeFileHandler(BaseFileHandler):

    def __init__(self, file_path: str = None):
        """
        FakeFileHandler constructor
        """

        if not isinstance(file_path, (str, type(None))):
            raise ValueError(f"Error file_path: {file_path} is not a str type")

        self.file = Mock()

    def __enter__(self):
        """
        __enter__
        @return: None
        @rtype: None
        """

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
