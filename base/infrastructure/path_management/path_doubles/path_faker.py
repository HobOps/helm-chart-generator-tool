# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_doubles import FileFaker
from base.infrastructure.path_management.path_validator import PathFormatValidator

# Domain
from base.domain.file_management.file_constants import file_type_values
from base.domain.path_management.path_constants import path_types_values
from base.domain.path_management.path_doubles import BasePath


class PathFaker(BasePath):
    """
    PathFaker
    """

    def __init__(self, target_path: str = None, target_path_type: str = None, fake_file: FileFaker = None):
        """
        PathFaker
        """

        if not isinstance(target_path, (str, type(None))):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        if not isinstance(target_path_type, (str, type(None))):
            raise ValueError(f"Error target_path_type: {target_path_type} is not str type")

        if not isinstance(fake_file, (FileFaker, type(None))):
            raise ValueError(f"Error fake_file: {fake_file} is not str type")

        valid_target_path = "/"

        if target_path is not None:
            valid_target_path = PathFormatValidator.validate_path_format(target_path=target_path)

        self.__fake_stored_path = dict()
        self.__fake_target_path = valid_target_path
        self.__fake_target_path_type = target_path_type or path_types_values.directory
        self.__fake_file = fake_file or FileFaker(file_name="fake_file_default", file_type_suffix=file_type_values.text)

    def as_posix(self):
        """
        as_posix
        @return: as_posix
        @rtype: str
        """

        return self.__fake_target_path

    def exists(self):
        """
        exists
        @return: exists
        @rtype: bool
        """

        if self.__fake_stored_path.get(self.__fake_target_path):
            return True

        return False

    def is_dir(self):
        """
        is_dir
        @return: is_dir
        @rtype: bool
        """

        if self.__fake_target_path_type == path_types_values.directory:
            return True

        return False

    def is_file(self):
        """
        is_file
        @return: is_file
        @rtype: bool
        """

        if self.__fake_target_path_type == path_types_values.file:
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

        path_split = relative_path.split(".")
        valid_file_types = [value for key, value in file_type_values.__dict__.items()]
        self.__fake_target_path_type = path_types_values.file if f".{path_split[1]}" in valid_file_types else path_types_values.directory

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

        self.__fake_stored_path[self.__fake_target_path] = "dir"

        return True

    @property
    def parent(self):
        """
        parent
        @return: path
        @rtype: str
        """

        path_in_parts = self.__fake_target_path.split("/")
        path_in_parts = path_in_parts[1:-1]
        path_parent = "/".join(path_in_parts)

        return path_parent

    def touch(self, exist_ok: bool = None):
        """
        touch
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        if self.__fake_target_path_type == path_types_values.file:

            self.__fake_stored_path[self.__fake_target_path] = self.__fake_file

    @property
    def suffix(self):
        """
        suffix
        @return: None
        @rtype: None
        """

        return self.__fake_file.suffix


