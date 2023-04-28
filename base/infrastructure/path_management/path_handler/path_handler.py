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

        if not self.__stored_path.is_dir():
            raise ValueError(f"Error stored_path: {self.__stored_path} is not a directory")

        self.__stored_path.mkdir(parents=True, exist_ok=True)

    def make_file(self, file_name: str, file_type_suffix: str, raw_enabled: bool = False, custom_suffix: str = None):
        """

        @param file_name:
        @type file_name:
        @param file_type_suffix:
        @type file_type_suffix:
        @param raw_enabled:
        @type raw_enabled:
        @param custom_suffix:
        @type custom_suffix:
        @return:
        @rtype:
        """

        if not isinstance(file_name, str):
            raise ValueError(f"Error file_name: {file_name} is not str type")

        if not isinstance(file_type_suffix, str):
            raise ValueError(f"Error file_type_suffix: {file_type_suffix} is not str type")

        if not isinstance(raw_enabled, bool):
            raise ValueError(f"Error raw_enabled: {raw_enabled} is not bool type")

        if not isinstance(custom_suffix, (str, type(None))):
            raise ValueError(f"Error custom_suffix: {custom_suffix} is not str type")

        if not self.__stored_path.exists():
            raise ValueError(f"Error stored_path: {self.__stored_path} doesn't exists")

        if not self.__stored_path.is_dir():
            raise ValueError(f"Error stored_path: {self.__stored_path} is not directory")

        if not FileTypeValidator.validate_file_type_suffix(file_type_suffix=file_type_suffix):
            raise ValueError(f"Error file_type_suffix: {file_type_suffix} is not valid file type")

        if not raw_enabled:
            file_address = f"{file_name}{file_type_suffix}"

        if raw_enabled:
            file_address = f"{file_name}{file_type_suffix}{custom_suffix}"

        self.__stored_path.joinpath(f"{file_address}")

        if not self.__stored_path.is_file():
            raise ValueError(f"Error stored_path: {self.__stored_path} is not file")

        if not self.__stored_path.suffix == file_type_suffix or self.__stored_path.suffix == f".{custom_suffix}":
            raise ValueError(f"Error stored_path: {self.__stored_path} suffix doesn't match the file_type: {file_type_suffix}")

        self.__stored_path.touch(exist_ok=True)

        if not self.__stored_path.exists():
            raise ValueError(f"Error stored_path: {self.__stored_path} something went wrong to create file")

    @property
    def stored_path(self):
        """
        stored_path
        @return: stored_path
        @rtype: BasePath
        """

        return self.__stored_path

