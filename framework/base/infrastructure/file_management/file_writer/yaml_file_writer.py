# coding: utf-8 -*-


import yaml


# Infrastructure
from framework.base.infrastructure.file_management.file_handler import FileHandler

# Domain
from framework.base.domain.common.value_objects import DictValueObject
from framework.base.domain.file_management.file_constants.file_mode_values import file_mode_values
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.file_management.file_handler import BaseFileHandler
from framework.base.domain.file_management.file_writer import BaseFileWriter
from framework.base.domain.path_management.path_doubles import BasePath


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

    def __init__(self, path_obj: BasePath, file_handler: BaseFileHandler = None):
        """
        YamlFileWriter constructor
        """

        if not isinstance(path_obj, BasePath):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_handler, (BaseFileHandler, type(None))):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        if not path_obj.exists():
            raise ValueError(f"Error path_obj: {path_obj} doesn't exists in file system")

        if not path_obj.suffix == file_type_values.yaml:
            raise ValueError(f"Error path_obj.suffix: {path_obj.suffix} it's not yaml type")

        self.__path_obj = path_obj
        self.__file_handler = file_handler or FileHandler(path_obj=self.__path_obj, file_mode=file_mode_values.write)

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

