# -*- coding: utf-8 -*-


import settings
from unittest.mock import Mock


# Infrastructure
from base.infrastructure.file_management.file_doubles import FileFaker
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.path_management.path_doubles import PathFaker
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.file_management.file_constants.file_mode_values import file_mode_values
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.path_management.path_constants.path_type_values import path_types_values


def test_file_handler_validation():
    """
    test_file_handler_validation
    """

    fake_data = """
    # My Fake Data
    Data:
      fake_data
    """

    fake_file = FileFaker(file_name="my_test_file", file_type_suffix=file_type_values.text, initial_content=fake_data)
    fake_file.open()

    target_folder_path = "/home/user1/project1/folder1"
    target_folder_path_type = path_types_values.directory

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=target_folder_path_type)

    target_file_path = "/home/user1/project1/folder1"
    target_file_path_type = path_types_values.file

    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=target_file_path_type, fake_file=fake_file, fake_parent_path=fake_folder_path)

    path_handler = PathHandler(path_obj=fake_file_path)
    path_handler.make_directory()
    path_handler.generate_path(file_name=fake_file.name, file_type_suffix=fake_file.suffix)

    with FileHandler(path_handler=path_handler, file_obj=fake_file, file_mode=file_mode_values.read) as file_handler:
        read_data = file_handler.read()

    assert read_data == fake_data


def test_file_handler_validation_read():
    """
    test_file_handler_validation_read
    """

    expected_data = '# Test\n\nLet see what happen\ngood luck\ncheers\n\n'

    file_path = '/config_files/input/configurations/my_read_test.txt'
    root_path = settings.get_root_path()
    target_path = root_path + file_path

    path_handler = PathHandler(target_path=target_path)

    with FileHandler(path_handler=path_handler, file_mode=file_mode_values.read) as file_handler:
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

    path_handler = PathHandler(target_path=target_path)

    with FileHandler(path_handler=path_handler, file_mode=file_mode_values.write) as file_handler:
        file_handler.write(expected_data)

    with FileHandler(path_handler=path_handler, file_mode=file_mode_values.read) as file_handler:
        read_data = file_handler.read()

    assert read_data == expected_data


def test_file_handler_validation_create_and_write():
    """
    test_file_handler_validation_create_and_write
    """

    expected_data = '# Test\n\nLet see what happen\ngood luck\ncheers\n\n'

    file_path = '/config_files/input/configurations/new_folder1/my_write_test.txt'
    root_path = settings.get_root_path()
    target_path = root_path + file_path

    path_handler = PathHandler(target_path=target_path)
    path_handler.make_directory()
    path_handler.generate_path()

    with FileHandler(path_handler=path_handler, file_mode=file_mode_values.write) as file_handler:
        file_handler.write(expected_data)

    with FileHandler(path_handler=path_handler, file_mode=file_mode_values.read) as file_handler:
        read_data = file_handler.read()

    assert read_data == expected_data







