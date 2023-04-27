# -*- coding: utf-8 -*-


# Infrastructure
from app.v2.modules.file_manager.infrastructure.manager import MainFileWriterCreator
from base.infrastructure.file_management.file_writer import JsonFileWriter
from base.infrastructure.file_management.file_writer import TextFileWriter
from base.infrastructure.file_management.file_writer import YamlFileWriter
from base.infrastructure.file_management.file_handler import FakeFile
from base.infrastructure.path_management.path_handler import FakePath
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.file_management.file_constants.file_type_values import file_type_values


def test_file_writer_creator_for_json_file_writer_type():
    """
    test_file_writer_creator_for_json_file_writer_type
    """

    fake_file = FakeFile(file_name="my_test", file_type_suffix=file_type_values.json)
    fake_path = FakePath(target_path="/home/user1/project1", fake_file=fake_file)
    path_handler = PathHandler(path_obj=fake_path)
    path_handler.make_directory()
    path_handler.make_file(file_name="my_test", file_type_suffix=file_type_values.json)

    file_writer_creator = MainFileWriterCreator(path_handler=path_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="json")

    assert isinstance(file_writer, JsonFileWriter)


def test_file_writer_creator_for_text_file_writer_type():
    """
    test_file_writer_creator_for_text_file_writer_type
    """

    fake_file = FakeFile(file_name="my_test", file_type_suffix=file_type_values.text)
    fake_path = FakePath(target_path="/home/user1/project1", fake_file=fake_file)
    path_handler = PathHandler(path_obj=fake_path)
    path_handler.make_directory()
    path_handler.make_file(file_name="my_test", file_type_suffix=file_type_values.text)

    file_writer_creator = MainFileWriterCreator(path_handler=path_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="text")

    assert isinstance(file_writer, TextFileWriter)


def test_file_writer_creator_for_yaml_file_writer_type():
    """
    test_file_writer_creator_for_yaml_file_writer_type
    """

    fake_file = FakeFile(file_name="my_test", file_type_suffix=file_type_values.yaml)
    fake_path = FakePath(target_path="/home/user1/project1", fake_file=fake_file)
    path_handler = PathHandler(path_obj=fake_path)
    path_handler.make_directory()
    path_handler.make_file(file_name="my_test", file_type_suffix=file_type_values.yaml)

    file_writer_creator = MainFileWriterCreator(path_handler=path_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="yaml")

    assert isinstance(file_writer, YamlFileWriter)




