# -*- coding: utf-8 -*-


from settings import Settings


# Infrastructure
from base.infrastructure.config_management.config_mapper import ConfigMapper
from base.infrastructure.config_management.config_reader import ConfigReader
from base.infrastructure.path_management.path_factory import SimplePathCreator

# Domain
from base.domain.path_management.path_doubles import BasePath


class AppConfigManager:
    """
    AppConfigManager
    """

    def __init__(self, path_obj: BasePath = None, config_data: dict = None):
        """
        AppConfigManager
        @param path_obj: path_obj
        @type path_obj: BasePath
        @param config_data: config_data
        @type config_data: dict
        """

        if not isinstance(path_obj, (BasePath, type(None))):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(config_data, (dict, type(None))):
            raise ValueError(f"Error config_data: {config_data} is not dict type")

        self.__path_obj = path_obj
        self.__config_data = config_data

    def parse_config(self, component_name: str):
        """
        parse_config
        @param component_name: component_name
        @type component_name: str
        @return: config_data
        @rtype: dict
        """

        root_path = Settings.get_root_path().as_posix()
        target_path = f"/config_files/input/configurations/{component_name}.ini"

        path_creator = SimplePathCreator(root_path=root_path)
        created_target_path = path_creator.generate_path(target_path=target_path, path_obj=self.__path_obj)

        filter_sections = [
            'DEFAULT',
        ]

        config_reader = ConfigReader(path_obj=created_target_path, config_data=self.__config_data)
        config_parser = config_reader.get_config_parser()
        config_mapper = ConfigMapper(
            config_parser=config_parser,
            filter_sections=filter_sections,
        )
        config_data = config_mapper.map_config_data()

        return config_data
