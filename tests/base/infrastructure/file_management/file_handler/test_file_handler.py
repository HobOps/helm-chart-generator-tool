# -*- coding: utf-8 -*-


from settings import Settings


# Infrastructure
from base.infrastructure.file_management.file_doubles import FileFaker
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.path_management.path_doubles import PathFaker
from base.infrastructure.path_management.path_factory import SimplePathCreator

# Domain
from base.domain.file_management.file_constants.file_mode_values import file_mode_values
from base.domain.file_management.file_constants.file_type_values import file_type_values
from base.domain.path_management.path_constants.path_type_values import path_types_values


def test_file_handler_validation_read():
    """
    test_file_handler_validation_read
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.text

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_data = """
    # My Fake Data
    Data:
      fake_data
    """

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix, initial_content=fake_data)
    fake_file.open()

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=path_types_values.file, file_obj=fake_file, parent_path=fake_folder_path)

    path_creator = SimplePathCreator(root_path=root_path)
    created_fake_file_path = path_creator.generate_path(path_obj=fake_file_path)

    with FileHandler(path_obj=created_fake_file_path, file_obj=fake_file, file_mode=file_mode_values.read) as file_handler:
        read_data = file_handler.read()

    assert read_data == fake_data


def test_file_handler_validation_write():
    """
    test_file_handler_validation_write
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.text

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_data = """
    # My Fake Data
    Data:
      fake_data
    """

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix, initial_content="")
    fake_file.open()

    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(target_path=target_file_path, target_path_type=path_types_values.file, file_obj=fake_file, parent_path=fake_folder_path)

    path_creator = SimplePathCreator(root_path=root_path)
    created_fake_file_path = path_creator.generate_path(path_obj=fake_file_path)

    with FileHandler(path_obj=created_fake_file_path, file_obj=fake_file, file_mode=file_mode_values.read) as file_handler:
        file_handler.write(fake_data)

    assert fake_file.content == fake_data
