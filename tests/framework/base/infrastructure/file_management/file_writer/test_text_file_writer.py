# -*- coding: utf-8 -*-


import pytest


# Infrastructure
from framework.base.infrastructure.file_management.file_doubles import FileFaker
from framework.base.infrastructure.file_management.file_handler import FileHandler
from framework.base.infrastructure.file_management.file_writer import TextFileWriter
from framework.base.infrastructure.path_management.path_doubles import PathFaker

# Domain
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.path_management.path_constants import path_types_values


def test_text_file_writer_validation_with_valid_params():
    """
    test_text_file_writer_validation_with_valid_params
    """

    data = [
        "data1",
        "data2",
        "data3",
        "data4",
    ]

    fake_file = FileFaker(file_name="fake_file_tester", file_type_suffix=file_type_values.text)
    fake_file.open()

    target_path = "/home/user1/project1/folder1"
    target_path = f"{target_path}/{fake_file.name}{fake_file.suffix}"

    fake_path = PathFaker(target_path=target_path, target_path_type=path_types_values.file, file_obj=fake_file)
    fake_path.touch()

    file_handler = FileHandler(path_obj=fake_path, file_obj=fake_file)

    text_file_writer = TextFileWriter(path_obj=fake_path, file_handler=file_handler)
    text_file_writer.write_file(data=data)

    assert fake_file.content == '\n'.join(data)


def test_text_file_writer_validation_with_invalid_path_not_exists():
    """
    test_text_file_writer_validation_with_invalid_path_not_exists
    """

    fake_file = FileFaker(file_name="fake_file_tester", file_type_suffix=file_type_values.yaml)
    fake_file.open()

    target_path = "/home/user1/project1/folder1"
    target_path = f"{target_path}/{fake_file.name}{fake_file.suffix}"

    fake_path = PathFaker(target_path=target_path, target_path_type=path_types_values.file, file_obj=fake_file)
    file_handler = FileHandler(path_obj=fake_path, file_obj=fake_file)

    expected_error_message = f"Error path_obj: {fake_path} doesn't exists in file system"

    with pytest.raises(ValueError) as err:
        text_file_writer = TextFileWriter(path_obj=fake_path, file_handler=file_handler)

    assert err.value.args[0] == expected_error_message


def test_text_file_writer_validation_with_invalid_file_type_suffix():
    """
    test_text_file_writer_validation_with_invalid_file_type_suffix
    """

    fake_file = FileFaker(file_name="fake_file_tester", file_type_suffix=file_type_values.yaml)
    fake_file.open()

    target_path = "/home/user1/project1/folder1"
    target_path = f"{target_path}/{fake_file.name}{fake_file.suffix}"

    fake_path = PathFaker(target_path=target_path, target_path_type=path_types_values.file, file_obj=fake_file)
    fake_path.touch()

    file_handler = FileHandler(path_obj=fake_path, file_obj=fake_file)

    expected_error_message = f"Error path_obj.suffix: {fake_path.suffix} it's not text type"

    with pytest.raises(ValueError) as err:
        text_file_writer = TextFileWriter(path_obj=fake_path, file_handler=file_handler)

    assert err.value.args[0] == expected_error_message


