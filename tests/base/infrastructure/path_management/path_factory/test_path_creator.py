# -*- coding: utf-8 -*-


import pytest


# Infrastructure
from base.infrastructure.path_management.path_doubles import PathFaker
from base.infrastructure.path_management.path_factory import PathItemCreator

# Domain
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.path_management.path_constants.path_type_values import path_types_values
from base.domain.path_management.path_doubles import BasePath


def test_path_creator_with_valid_params():
    """
    test_path_creator_with_valid_params
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.text

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=path_types_values.file, fake_parent_path=fake_folder_path)

    path_creator = PathItemCreator(
        root_path=root_path,
        project_path=project_path,
        folder_path=folder_path,
        file_name=file_name,
        file_type_suffix=file_type_suffix,
    )

    fake_path_created = path_creator.generate_path(path_obj=fake_file_path)

    assert path_creator.root_path == root_path
    assert path_creator.project_path == target_folder_path
    assert path_creator.target_path == target_file_path
    assert fake_path_created.as_posix() == target_file_path
    assert fake_path_created.exists() is True
    assert fake_path_created.is_file() is True
    assert isinstance(fake_path_created, BasePath) is True


def test_path_creator_with_valid_file_raw_enabled_params():
    """
    test_path_creator_with_valid_file_raw_enabled_params
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.raw
    file_raw_custom_suffix = "values.toml"

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}{file_raw_custom_suffix}"

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=path_types_values.file, fake_parent_path=fake_folder_path)

    path_creator = PathItemCreator(
        root_path=root_path,
        project_path=project_path,
        folder_path=folder_path,
        file_name=file_name,
        file_type_suffix=file_type_suffix,
        file_raw_enabled=True,
        file_raw_custom_suffix=file_raw_custom_suffix,
    )

    fake_path_created = path_creator.generate_path(path_obj=fake_file_path)

    assert path_creator.root_path == root_path
    assert path_creator.project_path == target_folder_path
    assert path_creator.target_path == target_file_path
    assert fake_path_created.as_posix() == target_file_path
    assert fake_path_created.exists() is True
    assert fake_path_created.is_file() is True
    assert isinstance(fake_path_created, BasePath) is True


def test_path_creator_with_not_valid_path_format():
    """
    test_path_creator_with_not_valid_path_format
    """

    invalid_root_path = "home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.text

    target_folder_path = f"{invalid_root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_folder_path = PathFaker(target_path=f"/{target_folder_path}", target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=f"/{target_file_path}", target_path_type=path_types_values.file, fake_parent_path=fake_folder_path)

    expected_error_message = f"Error target_path: home/user1 is not a valid path format"

    with pytest.raises(ValueError) as err:

        path_creator = PathItemCreator(
            root_path=invalid_root_path,
            project_path=project_path,
            folder_path=folder_path,
            file_name=file_name,
            file_type_suffix=file_type_suffix,
        )

    assert err.value.args[0] == expected_error_message


def test_path_creator_with_not_valid_file_type_suffix():
    """
    test_path_creator_with_not_valid_file_type_suffix
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = "not_valid_suffix"

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=path_types_values.file, fake_parent_path=fake_folder_path)

    expected_error_message = f"Error file_type_suffix: not_valid_suffix is not a valid file_type_suffix"

    with pytest.raises(ValueError) as err:

        path_creator = PathItemCreator(
            root_path=root_path,
            project_path=project_path,
            folder_path=folder_path,
            file_name=file_name,
            file_type_suffix=file_type_suffix,
        )

    assert err.value.args[0] == expected_error_message


def test_path_creator_with_not_valid_raw_activation():
    """
    test_path_creator_with_not_valid_raw_activation
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.raw
    file_raw_enabled = True

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=path_types_values.file, fake_parent_path=fake_folder_path)

    expected_error_message = f"Error file_raw_custom_suffix: {None} can't be None when is file_raw_enabled: {file_raw_enabled}"

    with pytest.raises(ValueError) as err:

        path_creator = PathItemCreator(
            root_path=root_path,
            project_path=project_path,
            folder_path=folder_path,
            file_name=file_name,
            file_type_suffix=file_type_suffix,
            file_raw_enabled=True,
        )

    assert err.value.args[0] == expected_error_message


def test_path_creator_with_not_valid_path_obj_to_generate():
    """
    test_path_creator_with_not_valid_path_obj_to_generate
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.raw
    file_raw_custom_suffix = "values.toml"

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}{file_raw_custom_suffix}"

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = 12345

    expected_error_message = f"Error path_obj: {fake_file_path} is not an instance of {BasePath}"

    path_creator = PathItemCreator(
        root_path=root_path,
        project_path=project_path,
        folder_path=folder_path,
        file_name=file_name,
        file_type_suffix=file_type_suffix,
        file_raw_enabled=True,
        file_raw_custom_suffix=file_raw_custom_suffix,
    )

    with pytest.raises(ValueError) as err:

        fake_path_created = path_creator.generate_path(path_obj=fake_file_path)

    assert err.value.args[0] == expected_error_message


