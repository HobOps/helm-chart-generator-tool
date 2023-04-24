# -*- coding: utf-8 -*-


import re
from pathlib import Path


# Domain
from base.domain.path_management.path_validator import BasePathDirectoryValidator


class PathDirectoryValidator(BasePathDirectoryValidator):
    """
    PathDirectoryValidator
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

        pattern = r"^(\/[a-z_\-\s0-9\.]+)"
        match_result = re.match(pattern=pattern, string=target_path)

        if not match_result:
            raise ValueError(f"Error target_path: {target_path} is not a valid path format")

        target_path_to_check = Path(target_path)

        if not target_path_to_check.exists():
            raise ValueError(f"Error target_path: {target_path} is not a valid directory path")

        if not target_path_to_check.is_dir():
            raise ValueError(f"Error target_path_to_check: {target_path_to_check} is not a directory")

        return target_path_to_check.absolute().__str__()
