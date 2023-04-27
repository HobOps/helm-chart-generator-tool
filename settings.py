# -*- coding: utf-8 -*-


from pathlib import Path


def get_root_path():
    """
    get_root_path
    @return: root_path_handler
    @rtype: BasePathHandler
    """

    root_path = Path(__file__).parent.__str__()

    return root_path


def get_app_version():
    """
    get_app_version
    @return:
    @rtype:
    """

    app_version = "version2"

    return app_version
