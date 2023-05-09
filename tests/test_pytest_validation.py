# -*- coding: utf-8 -*-


import pytest


from settings import Settings


def test_pytest_version_validation():
    """
    test_pytest_version_validation
    """

    assert "7.3.1" == str(pytest.__version__)


def test_pytest_root_path_validation():
    """
    test_pytest_root_path_validation
    """

    root_path = Settings.get_root_path()

    assert root_path is not None
