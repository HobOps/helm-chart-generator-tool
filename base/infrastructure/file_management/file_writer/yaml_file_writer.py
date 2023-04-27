# coding: utf-8 -*-


import yaml


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.common.value_objects import DictValueObject
from base.domain.file_management.file_constants import file_mode_values
from base.domain.file_management.file_constants import file_type_values
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.file_management.file_writer import BaseFileWriter
from base.domain.path_management.path_handler import BasePathHandler


def str_presenter(dumper, data):
    """
    str_presenter
    @param dumper: dumper
    @type dumper: dumper
    @param data: data
    @type data: data
    @return:
    @rtype:
    """

    multiline_checks = len(data.splitlines()) > 1

    if multiline_checks:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


class YamlFileWriter(BaseFileWriter):
    """
    YamlFileWriter
    """

    def __init__(self, path_handler: BasePathHandler = None, file_handler: BaseFileHandler = None):
        """
        YamlFileWriter constructor
        """

        if not isinstance(path_handler, (BasePathHandler, type(None))):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        self.__path_handler = path_handler or PathHandler(target_path='/')

        if not self.__path_handler.stored_path.exists():
            raise ValueError(f"Error stored_path: {self.__path_handler.stored_path} doesn't exists in file system")

        if self.__path_handler.stored_path.suffix != file_type_values.yaml:
            raise ValueError(f"Error path_handler: {path_handler} file_type_suffix is not .yaml")

        self.__file_handler = file_handler or FileHandler(
            file_mode=file_mode_values.write,
            path_handler=path_handler,
        )

    def write_file(self, data: dict):
        """
        write_file
        @param data: data
        @type data: dict
        @return: None
        @rtype: None
        """

        if not isinstance(data, dict):
            raise ValueError(f"Error data: {data} is not dict type")

        data_value = DictValueObject(data)

        yaml.add_representer(str, str_presenter)
        yaml.representer.SafeRepresenter.add_representer(str, str_presenter)

        with self.__file_handler as yaml_file_handler:
            yaml.dump(data_value.value, yaml_file_handler, default_flow_style=False, sort_keys=False)

