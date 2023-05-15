# -*- coding: utf-8 -*-


from settings import Settings


# Infrastructure
from base.infrastructure.config_management.config_mapper import ConfigMapper
from base.infrastructure.config_management.config_reader import ConfigReader
from base.infrastructure.path_management.path_factory import SimplePathCreator


class AppConfigManager:
    """
    AppConfigManager
    """

    @staticmethod
    def parse_config(component_name: str):
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
        created_target_path = path_creator.generate_path(target_path=target_path)

        filter_sections = [
            'DEFAULT',
        ]

        config_reader = ConfigReader(path_obj=created_target_path)
        config_parser = config_reader.get_config_parser()
        config_mapper = ConfigMapper(
            config_parser=config_parser,
            filter_sections=filter_sections,
        )
        config_data = config_mapper.map_config_data()

        return config_data
