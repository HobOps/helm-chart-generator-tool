# -*- coding: utf-8 -*-


import pytest


# Infrastructure
from base.infrastructure.file_management.file_handler import FakeFile
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.file_management.file_writer import YamlFileWriter
from base.infrastructure.path_management.path_handler import FakePath
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.path_management.path_constants.path_type_values import path_types_values


def test_yaml_file_writer_validation_with_valid_params():
    """
    test_yaml_file_writer_validation_with_valid_params
    """

    expected_content = 'Nonekey1: data1\nkey2: data2\nkey3:\n  key31: data31\n  key32: data32\n'

    data = {
        "key1": "data1",
        "key2": "data2",
        "key3": {
            "key31": "data31",
            "key32": "data32"
        }
    }

    fake_file = FakeFile(file_name="fake_file_tester", file_type_suffix=file_type_values.yaml)
    fake_file.open()

    target_path = "/home/user1/project1/folder1"
    target_path = f"{target_path}/{fake_file.name}{fake_file.suffix}"
    fake_path = FakePath(target_path=target_path, target_path_type=path_types_values.file, fake_file=fake_file)
    fake_path.touch()

    path_handler = PathHandler(path_obj=fake_path)
    file_handler = FileHandler(file_obj=fake_file)

    yaml_file_writer = YamlFileWriter(path_handler=path_handler, file_handler=file_handler)
    yaml_file_writer.write_file(data=data)

    assert fake_file.content == expected_content


def test_yaml_file_writer_validation_with_invalid_path_not_exists():
    """
    test_yaml_file_writer_validation_with_invalid_path_not_exists
    """

    fake_file = FakeFile(file_name="fake_file_tester", file_type_suffix=file_type_values.yaml)
    fake_file.open()

    target_path = "/home/user1/project1/folder1"
    target_path = f"{target_path}/{fake_file.name}{fake_file.suffix}"
    fake_path = FakePath(target_path=target_path, target_path_type=path_types_values.file, fake_file=fake_file)

    path_handler = PathHandler(path_obj=fake_path)
    file_handler = FileHandler(file_obj=fake_file)

    expected_error_message = f"Error stored_path: {path_handler.stored_path} doesn't exists in file system"

    with pytest.raises(ValueError) as err:
        yaml_file_writer = YamlFileWriter(path_handler=path_handler, file_handler=file_handler)

    assert err.value.args[0] == expected_error_message


def test_yaml_file_writer_validation_with_invalid_file_type():
    """
    test_yaml_file_writer_validation_with_invalid_file_type
    """

    fake_file = FakeFile(file_name="fake_file_tester", file_type_suffix=file_type_values.json)
    fake_file.open()

    target_path = "/home/user1/project1/folder1"
    target_path = f"{target_path}/{fake_file.name}{fake_file.suffix}"
    fake_path = FakePath(target_path=target_path, target_path_type=path_types_values.file, fake_file=fake_file)
    fake_path.touch()

    path_handler = PathHandler(path_obj=fake_path)
    file_handler = FileHandler(file_obj=fake_file)

    expected_error_message = f"Error path_handler: {path_handler} file_type_suffix is not .yaml"

    with pytest.raises(ValueError) as err:
        yaml_file_writer = YamlFileWriter(path_handler=path_handler, file_handler=file_handler)

    assert err.value.args[0] == expected_error_message


