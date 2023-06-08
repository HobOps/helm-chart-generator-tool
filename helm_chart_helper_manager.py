# -*- coding: utf-8 -*-


import argparse


# Application
from app.app_management import AppVersionCreator
from app.app_management import ArgumentData
from app.v1.script import AppMainManagerV10
from app.v2.main import AppMainManagerV21
from app.v2.main import AppMainManagerV22


class HelmChartHelperManager:
    """
    HelmChartHelperManager
    """

    @staticmethod
    def run(name: str = None, version: str = None):
        """
        run
        @return: None
        @rtype: None
        """

        if not isinstance(name, str):
            raise ValueError(f"Error name: {name} is not str type")

        if not isinstance(version, str):
            raise ValueError(f"Error version: {version} is not str type")

        argument_data = ArgumentData(name=name, version=version)

        # Parses program arguments
        args_parser = argparse.ArgumentParser(description='Generates a helm charts from components on a kubernetes cluster.')
        args_parser.add_argument('--name', action='store', type=str, help="Name of the helm chart")
        args_parser.add_argument('--version', action='store', type=str, help="Version number in script")
        arguments = args_parser.parse_args()

        args = argument_data or ArgumentData(name=arguments.name, version=arguments.version)

        app_version_factory = AppVersionCreator()
        app_manager = app_version_factory.create_app(args.version)
        app_manager.run(args=args)


if __name__ == "__main__":
    helper_manager = HelmChartHelperManager()
    helper_manager.run()
