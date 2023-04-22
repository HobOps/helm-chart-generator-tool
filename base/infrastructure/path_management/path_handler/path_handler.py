# -*- coding: utf-8 -*-


from pathlib import Path


# Domain
from base.domain.path_management.path_handler import BasePathHandler


class PathHandler(BasePathHandler):
    """
    PathHandler
    """

    def __init__(self, root_path: str = None, current_path: str = None, target_path: str = None, expected_path: str = None):
        """
        BasePathHandler
        """

        if not isinstance(root_path, (str, type(None))):
            raise ValueError(f"Error root_pah: {root_path} is not str type")

        if not isinstance(target_path, (str, type(None))):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        if not isinstance(current_path, (str, type(None))):
            raise ValueError(f"Error current_path: {current_path} is not str type")

        if not isinstance(expected_path, (str, type(None))):
            raise ValueError(f"Error expected_path: {expected_path} is not str type")

        self.__root_path = current_path or Path(root_path).parent.__str__()
        self.__target_path = expected_path or Path(target_path).parent.__str__()

    def join_path(self, target_path: str):
        """
        join_path
        @return: joined_path
        @rtype: Path
        """

        if not isinstance(target_path, str):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        self.__target_path = Path(f"{self.__root_path}/{target_path}").__str__()

    @property
    def root_path(self) -> str:
        """
        root_path
        @return: root_path
        @rtype: str
        """

        return self.__root_path

    @property
    def target_path(self) -> str:
        """
        target_path
        @return: target_path
        @rtype: str
        """

        return self.__target_path

