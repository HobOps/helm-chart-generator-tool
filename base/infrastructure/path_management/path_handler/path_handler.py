# -*- coding: utf-8 -*-


from pathlib import Path


# Domain
from base.domain.path_management.path_handler import BasePathHandler


class PathHandler(BasePathHandler):
    """
    PathHandler
    """

    def __init__(self, root_path):
        """
        BasePathHandler
        """

        self.__root_path = Path(root_path).parent
        self.__target_path = ""

    def join_path(self, target_path):
        """
        join_path
        @return: joined_path
        @rtype: str
        """

        self.__target_path = Path(f"{self.__root_path}/{target_path}")

    @property
    def root_path(self):
        """
        root_path
        @return: root_path
        @rtype: str
        """

        return self.__root_path

    @property
    def target_path(self):
        """
        target_path
        @return: target_path
        @rtype: str
        """

        return self.__target_path

