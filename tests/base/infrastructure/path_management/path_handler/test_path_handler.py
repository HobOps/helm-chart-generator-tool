# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.path_management.path_handler import FakePath
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.path_management.path_constants.path_type_values import path_types_values


def test_path_handler_with_valid_params():
    """
    test_path_handler_with_valid_params
    """

    target_path = "/home/user1/project1/folder1"
    target_path_type = path_types_values.directory

    fake_path = FakePath(target_path=target_path, target_path_type=target_path_type)
    path_handler = PathHandler(path_obj=fake_path)

    assert path_handler.stored_path.exists() is False

    path_handler.make_directory()

    assert path_handler.stored_path.exists() is True
    assert path_handler.stored_path.is_dir() is True
    assert path_handler.stored_path.is_file() is False

    path_handler.make_file(file_name="fake_file_name", file_type_suffix=file_type_values.text)

    assert path_handler.stored_path.exists() is True
    assert path_handler.stored_path.is_dir() is False
    assert path_handler.stored_path.is_file() is True
    assert path_handler.stored_path.suffix == file_type_values.text



