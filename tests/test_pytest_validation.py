# -*- coding: utf-8 -*-


import pytest


def test_pytest_version_validation():
    """
    test_pytest_version_validation
    """

    assert "7.3.1" == str(pytest.__version__)


def test_pytest_print_validation():
    """
    test_pytest_print_validation
    """

    info = f"We are using Pytest: {pytest.__version__}"

    print(info)

    assert "We are using Pytest: 7.3.1" == info
    