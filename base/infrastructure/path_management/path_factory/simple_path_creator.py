# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_validator import FileTypeValidator
from base.infrastructure.path_management.path_doubles import PathItem
from base.infrastructure.path_management.path_validator import PathFormatValidator

# Domain
from base.domain.path_management.path_doubles import BasePath
from base.domain.path_management.path_factory import BasePathCreator


class SimplePathCreator(BasePathCreator):
    """
    SimplePathCreator
    """

    def __init__(self, root_path: str = None, target_path: str = None):
        """
        SimplePathCreator constructor
        @param root_path: root_path
        @type root_path: str
        @param target_path: target_path
        @type target_path: str
        """

        if not isinstance(root_path, (str, type(None))):
            raise ValueError(f"Error root_path: {root_path} is not str type")

        if not isinstance(target_path, (str, type(None))):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        PathFormatValidator.validate_path_format(root_path)
        PathFormatValidator.validate_path_format(target_path)
        PathFormatValidator.validate_path_format(root_path + target_path)

        self.__root_path = root_path
        self.__target_path = root_path + target_path
        self.__stored_path = ""

    def generate_path(self, path_obj: BasePath = None) -> BasePath:
        """
        generate_path
        @param path_obj: path_obj
        @type path_obj: BasePath
        @return: stored_path
        @rtype: BasePath
        """

        if not isinstance(path_obj, (BasePath, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        self.__stored_path = path_obj or PathItem(target_path=self.__target_path)

        self.__stored_path.parent.mkdir(parents=True, exist_ok=True)
        self.__stored_path.touch(exist_ok=True)

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
    def target_path(self):
        """
        target_path
        @return: target_path
        @rtype: str
        """

        return self.__target_path

