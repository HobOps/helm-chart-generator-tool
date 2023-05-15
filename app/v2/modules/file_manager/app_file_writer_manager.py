# -*- coding: utf-8 -*-


from typing import Any
from settings import Settings


# Infrastructure
from base.infrastructure.file_management.file_creator import FileWriterCreator
from base.infrastructure.path_management.path_factory import SimplePathCreator

# Domain
from base.domain.path_management.path_doubles import BasePath
from base.domain.file_management.file_handler import BaseFileHandler


class AppFileWriterManager:
    """
    AppFileWriterManager
    """

    def __init__(self, path_obj: BasePath = None, file_handler: BaseFileHandler = None):
        """
        AppFileWriterManager constructor
        @param path_obj: path_obj
        @type path_obj: BasePath
        @param file_handler: file_handler
        @type file_handler: BaseFileHandler
        """

        if not isinstance(path_obj, (BasePath, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        self.__path_obj = path_obj
        self.__file_handler = file_handler

    def write_file(self, path: str, values: Any, mode: str):
        """
        write_file
        @param path: path
        @type path: str
        @param values: values
        @type values: Any
        @param mode: mode
        @type mode: str
        @return: None
        @rtype: None
        """

        if not isinstance(path, str):
            raise ValueError(f"Error path: {path} is not str type")

        if not isinstance(mode, str):
            raise ValueError(f"Error mode: {mode} is not str type")

        root_path = Settings.get_root_path().as_posix()
        target_path = f"/{path}"

        file_path_creator = SimplePathCreator(root_path=root_path)
        file_path = file_path_creator.generate_path(target_path=target_path, path_obj=self.__path_obj)

        file_writer_creator = FileWriterCreator(path_obj=file_path, file_handler=self.__file_handler)
        file_writer = file_writer_creator.create_file_writer(file_type=mode)
        file_writer.write_file(data=values)
