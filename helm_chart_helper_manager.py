# -*- coding: utf-8 -*-


import argparse


# Application
from app.v2.main import AppMainManager


class HelmChartHelperManager:
    """
    HelmChartHelperManager
    """

    @staticmethod
    def run():
        """
        run
        @return: None
        @rtype: None
        """

        # Parses program arguments
        args_parser = argparse.ArgumentParser(description='Generates a helm charts from components on a kubernetes cluster.')
        args_parser.add_argument('--name', action='store', type=str, help="Name of the helm chart")
        args_parser.add_argument('--version', action='store', type=str, help="Version number in script")
        args = args_parser.parse_args()

        app_main = AppMainManager()
        app_main.run(args)


if __name__ == "__main__":
    helper_manager = HelmChartHelperManager()
    helper_manager.run()

