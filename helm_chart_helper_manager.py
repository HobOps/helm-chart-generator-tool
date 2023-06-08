# -*- coding: utf-8 -*-


import argparse


# Application
from app.v1.script import AppMainManagerV10
from app.v2.main import AppMainManagerV21
from app.v2.main import AppMainManagerV22


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

        if int(args.version) == 10:
            app_main1 = AppMainManagerV10()
            app_main1.run(args)

        if int(args.version) == 21:
            app_main1 = AppMainManagerV21()
            app_main1.run(args)

        if int(args.version) == 22:
            app_main1 = AppMainManagerV22()
            app_main1.run(args)


if __name__ == "__main__":
    helper_manager = HelmChartHelperManager()
    helper_manager.run()

