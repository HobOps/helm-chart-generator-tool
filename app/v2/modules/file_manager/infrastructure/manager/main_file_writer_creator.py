# -*- coding: utf-8 -*-


from typing import Callable


# Infrastructure
from base.infrastructure.file_management.file_writer import TextFileWriter
from base.infrastructure.file_management.file_writer import JsonFileWriter
from base.infrastructure.file_management.file_writer import YamlFileWriter

# Domain
from app.v2.modules.file_manager.domain.services.create import FileWriterCreator
from base.domain.file_management.file_constants import file_types_values
from base.domain.file_management.file_writer import BaseFileWriter


class MainFileWriterCreator(FileWriterCreator):
    """
    MainFileWriterCreator
    """

    @classmethod
    def create_file_writer(cls, file_type: str) -> BaseFileWriter:
        """
        create_writer
        @param file_type: file_type
        @type file_type:
        @return: BaseFileWriter
        @rtype: BaseFileWriter
        """

        if not isinstance(file_type, str):
            raise ValueError(f"Error file_type: {file_type} is not str type")

        if file_type not in file_types_values:
            raise ValueError(f"Error file_type: {file_type} is not a valid file type")

        file_writer_type = f"{file_type}_file_writer"

        return cls.file_writer_factory(file_writer_type)

    @classmethod
    def file_writer_factory(cls, file_writer_type: Callable) -> BaseFileWriter:
        """
        file_writer_callback
        @param file_writer_type: file_writer_type
        @type file_writer_type: Callable
        @return: file_writer
        @rtype: BaseFileWriter
        """

        return file_writer_type()

    @staticmethod
    def yaml_file_writer() -> YamlFileWriter:
        """
        yaml_file_writer
        @return: yaml_file_writer
        @rtype: YamlFileWriter
        """

        return YamlFileWriter()

    @staticmethod
    def json_file_writer() -> JsonFileWriter:
        """
        json_file_writer
        @return: json_file_writer
        @rtype: YamlFileWriter
        """

        return JsonFileWriter()

    @staticmethod
    def text_file_writer() -> TextFileWriter:
        """
        text_file_writer
        @return: text_file_writer
        @rtype: YamlFileWriter
        """

        return TextFileWriter()
