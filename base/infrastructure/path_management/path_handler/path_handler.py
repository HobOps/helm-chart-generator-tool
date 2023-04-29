# -*- coding: utf-8 -*-


from pathlib import Path


# Infrastructure
from base.infrastructure.file_management.file_validator import FileTypeValidator
from base.infrastructure.path_management.path_validator import PathFormatValidator

# Domain
from base.domain.path_management.path_doubles import BasePath
from base.domain.path_management.path_handler import BasePathHandler


class PathHandler(BasePathHandler):
    """
    PathHandler
    """

    def __init__(self, target_path: str = None, path_obj: BasePath = None):
        """
        PathHandler
        @param target_path: target_path
        @type target_path: str
        @param path_obj: path_obj
        @type path_obj: BasePath
        """

        if not isinstance(target_path, (str, type(None))):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        if not isinstance(path_obj, (BasePath, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not {BasePath} type")

        valid_target_path = "/"

        if target_path is not None:
            valid_target_path = PathFormatValidator.validate_path_format(target_path)

        self.__stored_path = path_obj or Path(valid_target_path)

    def make_directory(self):
        """
        make_directory
        @return: None
        @rtype: None
        """

        self.__stored_path.parent.mkdir(parents=True, exist_ok=True)

    def make_file(self, file_name: str = None, file_type_suffix: str = None):
        """
        make_file
        @return:
        @rtype:
        """

        if not self.__stored_path.parent.exists():
            raise ValueError(f"Error stored_path: {self.__stored_path.parent} needs to exists before file creation")

        self.__stored_path.touch(exist_ok=True)

    @property
    def stored_path(self):
        """
        stored_path
        @return: stored_path
        @rtype: path
        """

        return self.__stored_path
