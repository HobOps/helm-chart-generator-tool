# -*- coding: utf-8 -*-


import re


# Domain
from base.domain.path_management.path_validator import BasePathFormatValidator


class PathFormatValidator(BasePathFormatValidator):
    """
    PathFormatValidator
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

        if not isinstance(target_path, str):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        pattern = r"^(\/[a-z_\-\s0-9\.]+)"
        match_result = re.match(pattern=pattern, string=target_path)

        if not match_result:
            raise ValueError(f"Error target_path: {target_path} is not a valid path format")

        return target_path
