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

    def __init__(self, target_path: str = None, target_path_type: str = None, parent_path: BasePath = None, file_obj: FileFaker = None):
        """
        PathFaker
        """

        if not isinstance(target_path, (str, type(None))):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        if not isinstance(target_path_type, (str, type(None))):
            raise ValueError(f"Error target_path_type: {target_path_type} is not str type")

        if not isinstance(parent_path, (BasePath, type(None))):
            raise ValueError(f"Error fake_parent_path: {parent_path} is not str type")

        if not isinstance(file_obj, (FileFaker, type(None))):
            raise ValueError(f"Error fake_file: {file_obj} is not str type")

        valid_target_path = "/"

        if target_path is not None:
            valid_target_path = PathFormatValidator.validate_path_format(target_path=target_path)

        self.__fake_stored_path = dict()
        self.__fake_target_path = valid_target_path
        self.__fake_target_path_type = target_path_type or path_types_values.directory
        self.__fake_target_path_parent_path = parent_path
        self.__fake_file = file_obj or FileFaker(file_name="fake_file_default", file_type_suffix=file_type_values.text)

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

        return self.__fake_target_path_parent_path

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


