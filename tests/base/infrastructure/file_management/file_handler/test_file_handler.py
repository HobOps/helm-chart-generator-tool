# -*- coding: utf-8 -*-


import settings
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


def test_file_handler_validation_read():
    """
    test_file_handler_validation_read
    """

    expected_data = '# Test\n\nLet see what happen\ngood luck\ncheers\n\n'

    file_path = '/config_files/input/configurations/my_read_test.txt'
    root_path = settings.get_root_path()
    target_path = root_path + file_path

    with FileHandler(file_path=target_path, file_mode=file_mode_values.read) as file_handler:
        read_data = file_handler.read()

    assert read_data == expected_data


def test_file_handler_validation_write():
    """
    test_file_handler_validation_write
    """

    expected_data = '# Test\n\nLet see what happen\ngood luck\ncheers\n\n'

    file_path = '/config_files/input/configurations/my_write_test.txt'
    root_path = settings.get_root_path()
    target_path = root_path + file_path

    with FileHandler(file_path=target_path, file_mode=file_mode_values.write) as file_handler:
        file_handler.write(expected_data)

    with FileHandler(file_path=target_path, file_mode=file_mode_values.read) as file_handler:
        read_data = file_handler.read()

    assert read_data == expected_data







