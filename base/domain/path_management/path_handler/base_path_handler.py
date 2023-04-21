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
    def join_path(self, target_path):
        """
        join_path
        @param target_path: target_path
        @type target_path:
        @return: target_path
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @property
    @abstractmethod
    def root_path(self):
        """
        root_path
        @return: root_path
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @property
    @abstractmethod
    def target_path(self):
        """
        target_path
        @return: target_path
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

