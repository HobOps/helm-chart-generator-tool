# -*- coding: utf-8 -*-


from pathlib import Path


# Infrastructure
from base.infrastructure.file_management.file_validator import FileTypeValidator
from base.infrastructure.path_management.path_doubles import PathItem
from base.infrastructure.path_management.path_validator import PathFormatValidator

# Domain
from base.domain.path_management.path_doubles import BasePath
from base.domain.path_management.path_handler import BasePathHandler


class PathHandler(BasePathHandler):
    """
    PathHandler
    """

    def __init__(
        self,
        file_name: str,
        file_type_suffix: str,
        folder_path: str = None,
        file_raw_enabled: bool = False,
        file_raw_custom_suffix: str = None,
        path_obj: BasePath = None,
        root_path: str = None,
        project_path: str = None,
    ):
        """
        PathHandler constructor
        @param file_name: file_name
        @type file_name: str
        @param file_type_suffix: file_type_suffix
        @type file_type_suffix: str
        @param folder_path: folder_path
        @type folder_path: str
        @param file_raw_enabled: file_raw_enabled
        @type file_raw_enabled: bool
        @param file_raw_custom_suffix: file_raw_custom_suffix
        @type file_raw_custom_suffix: str
        """

        if not isinstance(root_path, (str, type(None))):
            raise ValueError(f"Error root_path: {root_path} is not str type")

        if not isinstance(project_path, (str, type(None))):
            raise ValueError(f"Error project_path: {project_path} is not str type")

        if not isinstance(file_name, str):
            raise ValueError(f"Error file_name: {file_name} is not str type")

        if not isinstance(file_type_suffix, str):
            raise ValueError(f"Error file_type_suffix: {file_type_suffix} is not str type")

        if not isinstance(folder_path, (str, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_raw_enabled, bool):
            raise ValueError(f"Error file_raw_enabled: {file_raw_enabled} is not bool type")

        if not isinstance(file_raw_custom_suffix, (str, type(None))):
            raise ValueError(f"Error file_raw_custom_suffix: {file_raw_custom_suffix} is not str type")

        if not isinstance(path_obj, (BasePath, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not FileTypeValidator.validate_file_type_suffix(file_type_suffix):
            raise ValueError(f"Error file_type_suffix: {file_type_suffix} is not a valid file_type_suffix")

        self.__root_path = root_path
        self.__project_path = project_path
        self.__path_file_type_validator = FileTypeValidator()
        self.__path_format_validator = PathFormatValidator()
        self.__target_path = ""
        self.__stored_path = ""

        self.__target_path = f"{self.__root_path}{self.__target_path}{folder_path}/{file_name}{file_type_suffix}"

        if file_raw_enabled:
            self.__target_path = self.__target_path + file_raw_custom_suffix

        if not PathFormatValidator.validate_path_format(self.__target_path):
            raise ValueError(f"Error full_path: {self.__target_path} has not valid path format")

    def generate_path(self, path_obj: BasePath) -> BasePath:
        """
        generate_path
        @param path_obj: path_obj
        @type path_obj: BasePath
        @return: stored_path
        @rtype: BasePath
        """

        if not isinstance(path_obj, BasePath):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        self.__stored_path = path_obj or PathItem(target_path=self.__target_path)

        self.__stored_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.__stored_path.parent.exists():
            raise ValueError(f"Error stored_path: {self.__stored_path.parent} needs to exists before file creation")

        self.__stored_path.touch(exist_ok=True)

        if not self.__stored_path.exists():
            raise ValueError(f"Error stored_path: {self.__stored_path.as_posix()} file is not created")

        return self.__stored_path

    @property
    def root_path(self):
        """
        root_path
        @return: root_path
        @rtype: str
        """

        return self.__root_path

    @property
    def project_path(self):
        """
        project_path
        @return: project_path
        @rtype: str
        """

        return self.__project_path

    @property
    def target_path(self):
        """
        target_path
        @return: target_path
        @rtype: str
        """

        return self.__target_path


