# coding: utf-8 -*-


import os
import yaml


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler

# Domain
from base.domain.common.value_objects import DictValueObject
from base.domain.file_management.file_constants import file_mode_values
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

    def __init__(self, path_handler: BasePathHandler):
        """
        YamlFileWriter constructor
        """

        if not isinstance(path_handler, BasePathHandler):
            raise ValueError(f"Error path_handler: {path_handler} is not an instance of {BasePathHandler}")

        self.__path_handler = path_handler

    def write_file(self, data: dict):
        """
        write_file
        @param data: data
        @type data: dict
        @return: None
        @rtype: None
        """

        data_value = DictValueObject(data)

        yaml.add_representer(str, str_presenter)
        yaml.representer.SafeRepresenter.add_representer(str, str_presenter)

        with FileHandler(file_path=self.__path_handler.target_path, file_mode=file_mode_values.write) as yaml_file_handler:
            yaml.dump(data_value.value, yaml_file_handler, default_flow_style=False, sort_keys=False)

