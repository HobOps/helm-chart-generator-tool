# -*- coding: utf-8 -*-


# Infrastructure
from framework.base.infrastructure.file_management.file_writer import JsonFileWriter
from framework.base.infrastructure.file_management.file_writer import RawFileWriter
from framework.base.infrastructure.file_management.file_writer import TextFileWriter
from framework.base.infrastructure.file_management.file_writer import YamlFileWriter

# Domain
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.file_management.file_creator import BaseFileWriterCreator
from framework.base.domain.file_management.file_writer import BaseFileWriter
from framework.base.domain.file_management.file_handler import BaseFileHandler
from framework.base.domain.path_management.path_doubles import BasePath


class FileWriterCreator(BaseFileWriterCreator):
    """
    FileWriterCreator
    """

    def __init__(self, path_obj: BasePath = None, file_handler: BaseFileHandler = None):
        """
        FileWriterCreator constructor
        """

        if not isinstance(path_obj, (BasePath, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        self.__path_obj = path_obj
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

        return JsonFileWriter(path_obj=self.__path_obj, file_handler=self.__file_handler)

    def raw_file_writer(self) -> RawFileWriter:
        """
        raw_file_writer
        @return: raw_file_writer
        @rtype: RawFileWriter
        """

        return RawFileWriter(path_obj=self.__path_obj, file_handler=self.__file_handler)

    def text_file_writer(self) -> TextFileWriter:
        """
        text_file_writer
        @return: text_file_writer
        @rtype: YamlFileWriter
        """

        return TextFileWriter(path_obj=self.__path_obj, file_handler=self.__file_handler)

    def yaml_file_writer(self) -> YamlFileWriter:
        """
        yaml_file_writer
        @return: yaml_file_writer
        @rtype: YamlFileWriter
        """

        return YamlFileWriter(path_obj=self.__path_obj, file_handler=self.__file_handler)

