# -*- coding: utf-8 -*-


from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BasePathFormatValidator(Protocol):
    """
    BasePathFormatValidator
    """

    @staticmethod
    def validate_path_format(target_path: str):
        """
        validate_path_format
        @param target_path: target_path
        @type target_path: str
        @return: valid_target_path
        @rtype: str
        """

        raise NotImplementedError(f"{BasePathFormatValidator.__class__.__name__} Interface Missing Implementation")

