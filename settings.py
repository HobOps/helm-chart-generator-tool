# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.path_management.path_handler import BasePathHandler


def get_root_path_handler():
    """
    get_root_path_handler
    @return: root_path_handler
    @rtype: BasePathHandler
    """

    root_path_handler = PathHandler(__file__)

    return root_path_handler
