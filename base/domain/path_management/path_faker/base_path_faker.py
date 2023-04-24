# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BasePathFaker(Protocol):
    """
    BasePathFaker
    """

    @abstractmethod
    def create_path(self, target_path: str):
        """
        create_path
        @param target_path: target_path
        @type target_path: str
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def validate_path(self, target_path: str = None):
        """
        validate_path
        @param target_path: target_path
        @type target_path: str
        @return: is_valid
        @rtype: bool
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    @property
    def stored_path(self):
        """
        stored_path
        @return: stored_path
        @rtype:
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
