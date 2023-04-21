# -*- coding: utf-8 -*-


import pytest
import settings


def test_pytest_version_validation():
    """
    test_pytest_version_validation
    """

    assert "7.3.1" == str(pytest.__version__)


def test_pytest_root_path_validation():
    """
    test_pytest_root_path_validation
    """

    path_handler = settings.get_root_path_handler()
    assert path_handler.root_path.name == 'helm-chart-generator-tool'
    assert True
