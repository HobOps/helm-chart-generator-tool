# -*- coding: utf-8 -*-


import re


# Domain
from base.domain.path_management.path_faker import BasePathFaker


class PathFaker(BasePathFaker):
    """
    PathFaker
    """

    def __init__(self):
        """
        PathFaker constructor
        """

        self.__path_tree = dict()

    def create_path(self, target_path: str):
        """
        create_path
        @param target_path: target_path
        @type target_path: str
        @return: None
        @rtype: None
        """

        pattern = r"^(\/[a-z_\-\s0-9\.]+)"
        match_result = re.match(pattern=pattern, string=target_path)

        if not match_result:
            raise ValueError(f"Error target_path: {target_path} is not a valid path format")

        self.__path_tree[f"{match_result.string}"] = ""

    def validate_path(self, target_path: str = None):
        """
        validate_path
        @return: is_valid
        @rtype: bool
        """

        pattern = r"^(\/[a-z_\-\s0-9\.]+)"
        path_to_validate = target_path or self.__path_tree
        match_result = re.match(pattern=pattern, string=path_to_validate)

        if not match_result:
            raise ValueError(f"Error target_path: {target_path} is not a valid path format")

        if not self.__path_tree.get(target_path):
            raise ValueError(f"Error target_path: {target_path} doesn't exists")

        return True

    @property
    def stored_path(self):
        """
        stored_path
        @return: stored_path
        @rtype: dict
        """

        return self.__path_tree
