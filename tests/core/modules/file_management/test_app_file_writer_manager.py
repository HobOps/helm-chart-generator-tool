# -*- coding: utf-8 -*-


import pytest


# Infrastructure
from framework.base.infrastructure.file_management.file_doubles import FileFaker
from framework.base.infrastructure.file_management.file_handler import FileHandler
from framework.base.infrastructure.path_management.path_doubles import PathFaker

# Application
from core.modules.file_management import AppFileWriterManager

# Domain
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.path_management.path_constants.path_type_values import path_types_values


def test_app_file_writer_manager_with_valid_params():
    """
    test_app_file_writer_manager_with_valid_params
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.yaml

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    expected_content = 'Nonekey1: data1\nkey2: data2\nkey3:\n  key31: data31\n  key32: data32\n'

    fake_data = {
        "key1": "data1",
        "key2": "data2",
        "key3": {
            "key31": "data31",
            "key32": "data32"
        }
    }

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix)
    fake_file.open()

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(
        target_path=target_file_path,
        target_path_type=path_types_values.file,
        file_obj=fake_file,
        parent_path=fake_folder_path
    )
    fake_file_path.touch()

    file_handler = FileHandler(path_obj=fake_file_path, file_obj=fake_file)

    file_writer_manager = AppFileWriterManager(root_path=root_path, path_obj=fake_file_path, file_handler=file_handler)
    file_writer_manager.write_file(path=target_file_path, values=fake_data, mode='yaml')

    assert fake_file.content == expected_content


def test_app_file_writer_manager_with_not_valid_params_for_values():
    """
    test_app_file_writer_manager_with_not_valid_params_for_values
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.yaml

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_data = None
    expected_error_message = f"Error values: {fake_data} can't be None"

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix)
    fake_file.open()

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(
        target_path=target_file_path,
        target_path_type=path_types_values.file,
        file_obj=fake_file,
        parent_path=fake_folder_path
    )
    fake_file_path.touch()

    file_handler = FileHandler(path_obj=fake_file_path, file_obj=fake_file)

    file_writer_manager = AppFileWriterManager(root_path=root_path, path_obj=fake_file_path, file_handler=file_handler)

    with pytest.raises(ValueError) as err:
        file_writer_manager.write_file(path=target_file_path, values=fake_data, mode='yaml')

    assert err.value.args[0] == expected_error_message

