# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BasePathDirectoryValidator(Protocol):
    """
    BasePathDirectoryValidator
    """

    @staticmethod
    def validate_directory(target_path: str):
        """
        validate_directory
        @param target_path: target_path
        @type target_path: str
        @return: target_path_to_check
        @rtype: str
        """

        raise NotImplementedError(f"{BasePathDirectoryValidator.__class__.__name__} Interface Missing Implementation")

