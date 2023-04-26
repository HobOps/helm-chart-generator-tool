# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BasePathHandler(Protocol):
    """
    BasePathHandler
    """

    @abstractmethod
    def __init__(self):
        """
        BasePathHandler
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def make_directory(self):
        """
        maker_directory
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def make_file(self, file_name: str, file_type: str):
        """
        make_file
        @param file_name: file_name
        @type file_name: str
        @param file_type: file_type
        @type file_type: str
        @return:
        @rtype:
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

