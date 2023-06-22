# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


# Domain
from framework.base.domain.path_management.path_doubles import BasePath


@runtime_checkable
class BasePathCreator(Protocol):
    """
    BasePathCreator
    """

    @abstractmethod
    def generate_path(self, target_path: str, path_obj: BasePath) -> BasePath:
        """
        generate_path
        @param target_path: target_path
        @type target_path: str
        @param path_obj: path_obj
        @type path_obj: BasePath
        @return: path
        @rtype: BasePath
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

