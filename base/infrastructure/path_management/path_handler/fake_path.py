# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.path_management.path_validator import PathFormatValidator

# Domain
from base.domain.path_management.path_handler import BasePath


class FakePath(BasePath):
    """
    FakePath
    """

    def __init__(self, target_path: str = None):
        """
        FakePath
        """

        if not isinstance(target_path, str):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        valid_target_path = PathFormatValidator.validate_path_format(target_path=target_path)

        self.__fake_store_path = dict()
        self.__fake_target_path = valid_target_path or "/"
        self.__fake_store_path[self.__fake_target_path] = "\n"

    def cwd(self):
        """
        cwd
        @return: path
        @rtype: str
        """

        return self.__fake_store_path[self.__fake_target_path]

    def exists(self):
        """
        exists
        @return: exists
        @rtype: bool
        """

        if self.__fake_store_path.get(self.__fake_target_path):
            return True

        return False

    def joinpath(self, relative_path: str):
        """
        joinpath
        @param relative_path: relative_path
        @type relative_path: str
        @return: None
        @rtype: None
        """

        self.__fake_target_path = f"{self.__fake_target_path}/{relative_path}"

        return self.__fake_target_path

    def mkdir(self, parents: bool = None, exist_ok: bool = None):
        """
        mkdir
        @param parents: parents
        @type parents: bool
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        if not self.exists():

            self.__fake_store_path[self.__fake_target_path] = "\n"


