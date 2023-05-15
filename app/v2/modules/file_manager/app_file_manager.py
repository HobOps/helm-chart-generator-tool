# -*- coding: utf-8 -*-


from typing import Any
from settings import Settings


# Infrastructure
from base.infrastructure.file_management.file_creator import FileWriterCreator
from base.infrastructure.path_management.path_factory import SimplePathCreator


class AppFileManager:
    """
    AppFileManager
    """

    @staticmethod
    def write_file(path: str, values: Any, mode: str):
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
        file_path = file_path_creator.generate_path(target_path=target_path)

        file_writer_creator = FileWriterCreator(path_obj=file_path)
        file_writer = file_writer_creator.create_file_writer(file_type=mode)
        file_writer.write_file(data=values)
