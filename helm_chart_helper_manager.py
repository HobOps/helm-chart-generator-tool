# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.cli_management.argument_parser import ArgumentParser

# Application
from app.app_management import AppVersionCreator
from app.app_management import ArgumentData
from app.app_management import AppManagerBase
from app.app_management import AppVersionCreatorBase

# Domain
from base.domain.cli_management.argument_parser import BaseArgumentParser


class HelmChartHelperManager:
    """
    HelmChartHelperManager
    """

    def __init__(self, args_parser: BaseArgumentParser = None, app_version_factory: AppVersionCreatorBase = None):
        """
        HelmChartHelperManager
        @param app_version_factory: app_version_factory
        @type app_version_factory: AppVersionCreatorBase
        """

        if not isinstance(args_parser, (BaseArgumentParser, type(None))):
            raise ValueError(f"Error args_parser: {args_parser} is not an instance of {BaseArgumentParser}")

        if not isinstance(app_version_factory, (AppVersionCreatorBase, type(None))):
            raise ValueError(f"Error app_version_factory: {app_version_factory} is not an instance of {AppVersionCreatorBase}")

        self.__app_version_factory = app_version_factory or AppVersionCreator()
        self.__args_parser = args_parser or ArgumentParser()

    def run(self):
        """
        run
        @return: app_version
        @rtype: str
        """

        arguments_config = {
            "name": "Config File Name",
            "version": "Script Version Str Number",
        }

        self.__args_parser.add_arguments(args_config=arguments_config)
        arguments = self.__args_parser.parse_arguments()

        args = ArgumentData(name=arguments['name'], version=arguments['version'])

        print(args)

        app_manager: AppManagerBase = self.__app_version_factory.create_app(args.version)
        app_version = app_manager.run(args=args)

        return app_version


if __name__ == "__main__":
    helper_manager = HelmChartHelperManager()
    helper_manager.run()
