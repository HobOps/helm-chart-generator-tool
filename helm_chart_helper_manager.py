# -*- coding: utf-8 -*-


import argparse


# Application
from app.app_management import AppVersionCreator
from app.app_management import ArgumentData
from app.app_management import AppManagerBase
from app.app_management import AppVersionCreatorBase


class HelmChartHelperManager:
    """
    HelmChartHelperManager
    """

    def __init__(self, args_parser: argparse.ArgumentParser = None, app_version_factory: AppVersionCreatorBase = None):
        """
        HelmChartHelperManager
        @param app_version_factory: app_version_factory
        @type app_version_factory: AppVersionCreatorBase
        """

        if not isinstance(args_parser, (argparse.ArgumentParser, type(None))):
            raise ValueError(f"Error args_parser: {args_parser} is not an instance of {argparse.ArgumentParser}")

        if not isinstance(app_version_factory, (AppVersionCreatorBase, type(None))):
            raise ValueError(f"Error app_version_factory: {app_version_factory} is not an instance of {AppVersionCreatorBase}")

        self.__app_version_factory = app_version_factory or AppVersionCreator()
        self.__args_parser = args_parser or argparse.ArgumentParser(
            description='Generates a helm charts from components on a kubernetes cluster.',
        )

    def run(self, name: str = None, version: str = None):
        """
        run
        @return: app_version
        @rtype: str
        """

        if not isinstance(name, str):
            raise ValueError(f"Error name: {name} is not str type")

        if not isinstance(version, str):
            raise ValueError(f"Error version: {version} is not str type")

        argument_data = ArgumentData(name=name, version=version)

        # Parses program arguments
        self.__args_parser.add_argument('--name', action='store', type=str, help="Name of the helm chart")
        self.__args_parser.add_argument('--version', action='store', type=str, help="Version number in script")
        arguments = self.__args_parser.parse_args()

        args = argument_data or ArgumentData(name=arguments.name, version=arguments.version)

        app_manager: AppManagerBase = self.__app_version_factory.create_app(args.version)
        app_version = app_manager.run(args=args)

        return app_version


if __name__ == "__main__":
    helper_manager = HelmChartHelperManager()
    helper_manager.run()
