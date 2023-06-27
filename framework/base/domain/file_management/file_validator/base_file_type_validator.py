# -*- coding: utf-8 -*-


from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseFileTypeValidator(Protocol):
    """
    BaseFileTypeValidator
    """

    @staticmethod
    def validate_file_type(file_type: str):
        """
        validate_file_type
        @param file_type: file_type
        @type file_type: str
        @return: is_valid
        @rtype: bool
        """

        raise NotImplementedError(f"{BaseFileTypeValidator.__class__.__name__} Interface Missing Implementation")

    @staticmethod
    def validate_file_type_suffix(file_type_suffix: str):
        """
        validate_file_type_suffix
        @param file_type_suffix: file_type_suffix
        @type file_type_suffix: str
        @return: is_valid
        @rtype: bool
        """

        raise NotImplementedError(f"{BaseFileTypeValidator.__class__.__name__} Interface Missing Implementation")


