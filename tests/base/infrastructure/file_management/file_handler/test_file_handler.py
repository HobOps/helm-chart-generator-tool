# -*- coding: utf-8 -*-


import os
from unittest.mock import Mock


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler

# Domain
from base.domain.file_management.file_constants import file_mode_values


def test_file_handler_validation():
    """
    test_file_handler_validation
    """

    fake_file_path = "/fake/path/fake_file.txt"
    file_mode = file_mode_values.read

    fake_data = """
    # My Fake Data
    Data:
      fake_data
    """

    read_function = Mock(return_value=fake_data)
    fake_file = Mock(read=read_function)

    with FileHandler(file_path=fake_file_path, file_obj=fake_file, file_mode=file_mode) as file_handler:
        read_data = file_handler.read()

    assert read_data == fake_data
    assert True


def test_file_handler_validation_real():
    """
    test_file_handler_validation_real
    """

    expected_data = '# Test\n\nLet see what happen\ngood luck\ncheers\n\n'

    file_path = '/home/yair.avalos/HobOps/workstation2/Projects/helm-chart-generator-tool/config_files/input/configurations/my_test.txt'
    file_mode = file_mode_values.read

    with FileHandler(file_path=file_path, file_mode=file_mode) as file_handler:
        read_data = file_handler.read()

    assert read_data == expected_data
    assert True







