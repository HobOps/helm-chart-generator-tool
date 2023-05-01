# -*- coding: utf-8 -*-


import pytest


# Infrastructure
from base.infrastructure.path_management.path_doubles import PathFaker
from base.infrastructure.path_management.path_factory import PathItemCreator

# Domain
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.path_management.path_constants.path_type_values import path_types_values


def test_path_handler_with_valid_params():
    """
    test_path_handler_with_valid_params
    """

    target_folder_path = "/home/user1/project1/folder1"
    target_folder_path_type = path_types_values.directory

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=target_folder_path_type)

    target_file_path = "/home/user1/project1/folder1/my_file1.txt"
    target_file_path_type = path_types_values.file

    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=target_file_path_type, fake_parent_path=fake_folder_path)
    path_handler = PathItemCreator(path_obj=fake_file_path)

    assert path_handler.stored_path.exists() is False

    path_handler.make_directory()

    assert path_handler.stored_path.parent.exists() is True
    assert path_handler.stored_path.parent.is_dir() is True
    assert path_handler.stored_path.exists() is False
    assert path_handler.stored_path.is_file() is True

    path_handler.generate_path(file_name="fake_file_name", file_type_suffix=file_type_values.text)

    assert path_handler.stored_path.exists() is True
    assert path_handler.stored_path.is_dir() is False
    assert path_handler.stored_path.is_file() is True
    assert path_handler.stored_path.suffix == file_type_values.text


def test_path_handler_validate_direct_touch_with_not_directory_assigned_fails():
    """
    test_path_handler_validate_direct_touch_fails_with_not_directory_assigned
    """

    target_folder_path = "/home/user1/project1/folder1"
    target_folder_path_type = path_types_values.directory

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=target_folder_path_type)

    target_file_path = "/home/user1/project1/folder1/my_file1.txt"
    target_file_path_type = path_types_values.file

    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=target_file_path_type, fake_parent_path=fake_folder_path)
    path_handler = PathItemCreator(path_obj=fake_file_path)

    assert path_handler.stored_path.parent.exists() is False

    expected_error_message = f"Error stored_path: {path_handler.stored_path.parent} needs to exists before file creation"

    with pytest.raises(ValueError) as err:
        path_handler.generate_path(file_name="fake_file_name", file_type_suffix=file_type_values.text)

    assert err.value.args[0] == expected_error_message


def test_path_handler_init_with_invalid_path_format_fails():
    """
    test_path_handler_init_with_invalid_path_format_fails
    """

    invalid_target_path = "home/user.1/project1-folder1"

    expected_error_message = f"Error target_path: {invalid_target_path} is not a valid path format"

    with pytest.raises(ValueError) as err:
        path_handler = PathItemCreator(target_path=invalid_target_path)

    assert err.value.args[0] == expected_error_message


def test_path_handler_make_file_with_invalid_file_type_fails():
    """
    test_path_handler_make_file_with_invalid_file_type_fails
    """

    target_path = "/home/user1/project1/folder1"
    target_path_type = path_types_values.directory

    fake_path = PathFaker(target_path=target_path, target_path_type=target_path_type)
    path_handler = PathItemCreator(path_obj=fake_path)
    path_handler.make_directory()

    file_type_suffix = ".not_valid_suffix"

    expected_error_message = f"Error file_type_suffix: {file_type_suffix} is not valid file type"

    with pytest.raises(ValueError) as err:
        path_handler.generate_path(file_name="fake_file_name", file_type_suffix=file_type_suffix)

    assert err.value.args[0] == expected_error_message




