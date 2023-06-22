# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseFileWriter(Protocol):
    """
    BaseFileWriter
    """

    @abstractmethod
    def write_file(self, data):
        """
        write_file
        @param data: data
        @type data: data
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

