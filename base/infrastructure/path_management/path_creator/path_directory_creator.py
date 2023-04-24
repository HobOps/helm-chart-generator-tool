# -*- coding: utf-8 -*-


import os


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

        directory = os.path.dirname(target_path)
        os.makedirs(directory, exist_ok=True)
