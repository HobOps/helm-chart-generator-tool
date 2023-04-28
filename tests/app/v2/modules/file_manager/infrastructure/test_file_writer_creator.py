# -*- coding: utf-8 -*-


# Infrastructure
from app.v2.modules.file_manager.infrastructure.manager import MainFileWriterCreator
from base.infrastructure.file_management.file_writer import JsonFileWriter
from base.infrastructure.file_management.file_writer import TextFileWriter
from base.infrastructure.file_management.file_writer import YamlFileWriter
from base.infrastructure.file_management.file_doubles import FileFaker
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.path_management.path_doubles import PathFaker
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.file_management.file_constants.file_mode_values import file_mode_values
from base.domain.file_management.file_constants.file_type_values import file_type_values


def test_file_writer_creator_for_json_file_writer_type():
    """
    test_file_writer_creator_for_json_file_writer_type
    """

    fake_file = FileFaker(file_name="my_test", file_type_suffix=file_type_values.json)
    fake_path = PathFaker(target_path="/home/user1/project1", fake_file=fake_file)

    path_handler = PathHandler(path_obj=fake_path)
    path_handler.make_directory()
    path_handler.make_file(file_name="my_test", file_type_suffix=file_type_values.json)

    file_handler = FileHandler(path_handler=path_handler, file_obj=fake_file, file_mode=file_mode_values.write)

    file_writer_creator = MainFileWriterCreator(path_handler=path_handler, file_handler=file_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="json")

    assert isinstance(file_writer, JsonFileWriter)


def test_file_writer_creator_for_text_file_writer_type():
    """
    test_file_writer_creator_for_text_file_writer_type
    """

    fake_file = FileFaker(file_name="my_test", file_type_suffix=file_type_values.text)
    fake_path = PathFaker(target_path="/home/user1/project1", fake_file=fake_file)

    path_handler = PathHandler(path_obj=fake_path)
    path_handler.make_directory()
    path_handler.make_file(file_name="my_test", file_type_suffix=file_type_values.text)

    file_handler = FileHandler(path_handler=path_handler, file_obj=fake_file, file_mode=file_mode_values.write)

    file_writer_creator = MainFileWriterCreator(path_handler=path_handler, file_handler=file_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="text")

    assert isinstance(file_writer, TextFileWriter)


def test_file_writer_creator_for_yaml_file_writer_type():
    """
    test_file_writer_creator_for_yaml_file_writer_type
    """

    fake_file = FileFaker(file_name="my_test", file_type_suffix=file_type_values.yaml)
    fake_path = PathFaker(target_path="/home/user1/project1", fake_file=fake_file)

    path_handler = PathHandler(path_obj=fake_path)
    path_handler.make_directory()
    path_handler.make_file(file_name="my_test", file_type_suffix=file_type_values.yaml)

    file_handler = FileHandler(path_handler=path_handler, file_obj=fake_file, file_mode=file_mode_values.write)

    file_writer_creator = MainFileWriterCreator(path_handler=path_handler, file_handler=file_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="yaml")

    assert isinstance(file_writer, YamlFileWriter)




