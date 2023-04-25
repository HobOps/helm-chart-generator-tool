# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FakeFile
from base.infrastructure.path_management.path_validator import PathFormatValidator

# Domain
from base.domain.file_management.file_handler import BaseFile
from base.domain.path_management.path_handler import BasePath


class FakePath(BasePath):
    """
    FakePath
    """

    def __init__(self, target_path: str = None, fake_file: FakeFile = None):
        """
        FakePath
        """

        if not isinstance(target_path, str):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        if not isinstance(fake_file, FakeFile):
            raise ValueError(f"Error fake_file: {fake_file} is not str type")

        valid_target_path = "/"

        if target_path is not None:
            valid_target_path = PathFormatValidator.validate_path_format(target_path=target_path)

        self.__fake_file = fake_file or FakeFile(file_name="fake_file_default", file_type_suffix="txt")
        self.__fake_store_path = dict()
        self.__fake_target_path = valid_target_path
        self.__fake_store_path[self.__fake_target_path] = "dir"

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

    def is_dir(self):
        """
        is_dir
        @return: is_dir
        @rtype: bool
        """

        if self.__fake_store_path[self.__fake_target_path] == "dir":
            return True

        return False

    def is_file(self):
        """
        is_file
        @return: is_file
        @rtype: bool
        """

        if isinstance(self.__fake_store_path[self.__fake_target_path], BaseFile):
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

            self.__fake_store_path[self.__fake_target_path] = "dir"

    def suffix(self):
        """
        suffix
        @return: None
        @rtype: None
        """

        self.__fake_file.suffix

    def touch(self, exist_ok: bool = None):
        """
        touch
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        if not self.exists():

            self.__fake_store_path[self.__fake_target_path] = self.__fake_file

