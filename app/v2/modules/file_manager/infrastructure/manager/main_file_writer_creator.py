# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_writer import JsonFileWriter
from base.infrastructure.file_management.file_writer import RawFileWriter
from base.infrastructure.file_management.file_writer import TextFileWriter
from base.infrastructure.file_management.file_writer import YamlFileWriter

# Domain
from app.v2.modules.file_manager.domain.services.create import FileWriterCreator
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.path_management.path_handler import BasePathHandler


class MainFileWriterCreator(FileWriterCreator):
    """
    MainFileWriterCreator
    """

    def __init__(self, path_handler: BasePathHandler = None, file_handler: BaseFileHandler = None):
        """
        MainFileWriterCreator constructor
        """

        if not isinstance(path_handler, (BasePathHandler, type(None))):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        self.__path_handler = path_handler
        self.__file_handler = file_handler

    def create_file_writer(self, file_type: str) -> BaseFileWriter:
        """
        create_writer
        @param file_type: file_type
        @type file_type:
        @return: BaseFileWriter
        @rtype: BaseFileWriter
        """

        if not isinstance(file_type, str):
            raise ValueError(f"Error file_type: {file_type} is not str type")

        if file_type not in [key for key, value in file_type_values.__dict__.items()]:
            raise ValueError(f"Error file_type: {file_type} is not a valid file type")

        file_writer_type_factory = getattr(self, f"{file_type}_file_writer")

        return file_writer_type_factory()

    def json_file_writer(self) -> JsonFileWriter:
        """
        json_file_writer
        @return: json_file_writer
        @rtype: YamlFileWriter
        """

        return JsonFileWriter(path_handler=self.__path_handler, file_handler=self.__file_handler)

    def raw_file_writer(self) -> RawFileWriter:
        """
        raw_file_writer
        @return: raw_file_writer
        @rtype: RawFileWriter
        """

        return RawFileWriter(path_handler=self.__path_handler, file_handler=self.__file_handler)

    def text_file_writer(self) -> TextFileWriter:
        """
        text_file_writer
        @return: text_file_writer
        @rtype: YamlFileWriter
        """

        return TextFileWriter(path_handler=self.__path_handler, file_handler=self.__file_handler)

    def yaml_file_writer(self) -> YamlFileWriter:
        """
        yaml_file_writer
        @return: yaml_file_writer
        @rtype: YamlFileWriter
        """

        return YamlFileWriter(path_handler=self.__path_handler, file_handler=self.__file_handler)

