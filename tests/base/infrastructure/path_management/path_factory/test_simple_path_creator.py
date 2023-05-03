# -*- coding: utf-8 -*-


import pytest


# Infrastructure
from base.infrastructure.path_management.path_doubles import PathFaker
from base.infrastructure.path_management.path_factory import SimplePathCreator

# Domain
from base.domain.path_management.path_constants.path_type_values import path_types_values


def test_simple_path_creator_with_valid_params():
    """
    test_simple_path_creator_with_valid_params
    """

    root_path = "/home/user1"
    project_path = "/project1/folder1"
    file_path = "/my_file1.txt"

    target_path = project_path + file_path
    full_path_folder = root_path + project_path
    full_path_file = root_path + target_path

    fake_folder_path = PathFaker(target_path=full_path_folder, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=full_path_file, target_path_type=path_types_values.file, fake_parent_path=fake_folder_path)

    path_creator = SimplePathCreator(root_path=root_path)
    created_path = path_creator.generate_path(path_obj=fake_file_path)

    assert path_creator.root_path == root_path
    assert path_creator.target_path == full_path_file
    assert created_path.as_posix() == full_path_file
    assert created_path.exists() is True


def test_simple_path_creator_with_not_valid_params():
    """
    test_simple_path_creator_with_not_valid_params
    """

    root_path = "/home/user1"
    project_path_not_valid = "project1/folder1"
    file_path = "/my_file1.txt"

    target_path = project_path_not_valid + file_path

    expected_error_message = f"Error target_path: {target_path} is not a valid path format"

    with pytest.raises(ValueError) as err:
        path_creator = SimplePathCreator(root_path=root_path)
        path_creator.generate_path(target_path=target_path)

    assert err.value.args[0] == expected_error_message

