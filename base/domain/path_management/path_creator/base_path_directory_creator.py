# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BasePathDirectoryCreator(Protocol):
    """
    BasePathDirectoryCreator
    """

    @staticmethod
    def create_directory(target_path: str):
        """
        create_directory
        @param target_path: target_path
        @type target_path: str
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{BasePathDirectoryCreator.__class__.__name__} Interface Missing Implementation")

