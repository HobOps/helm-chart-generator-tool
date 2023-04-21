# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseFile(Protocol):
    """
    BaseFile
    """

    @abstractmethod
    def __init__(self):
        """
        BaseFile constructor
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def read(self):
        """
        read
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def write(self, data_to_write: str):
        """
        write
        @param data_to_write: data_to_write
        @type data_to_write: str
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def close(self):
        """
        read
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

