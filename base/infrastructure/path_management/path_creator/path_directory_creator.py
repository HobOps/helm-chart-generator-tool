# -*- coding: utf-8 -*-


import re
import os
import pathlib

# Domain
from base.domain.path_management.path_creator import BasePathDirectoryCreator


class PathDirectoryCreator(BasePathDirectoryCreator):
    """
    PathDirectoryCreator
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

        if not isinstance(target_path, str):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        pattern = r"^(\/[a-z_\-\s0-9\.]+)"
        match_result = re.match(pattern=pattern, string=target_path)

        if not match_result:
            raise ValueError(f"Error target_path: {target_path} is not a valid path format")

        directory = os.path.dirname(target_path)
        os.makedirs(directory, exist_ok=True)
