# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseFileHandler(Protocol):

    @abstractmethod
    def __init__(self):
        """
        BaseFileHandler constructor
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def __enter__(self):
        """
        __enter__
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
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

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
