# -*- coding: utf-8 -*-


from pathlib import Path


class Settings:
    """
    Settings
    """

    @staticmethod
    def get_root_path():
        """
        get_root_path
        @return: root_path_handler
        @rtype: Path
        """

        root_path = Path(__file__).parent

        return root_path

    @staticmethod
    def get_app_version():
        """
        get_app_version
        @return:
        @rtype:
        """

        app_version = "version2"

        return app_version
