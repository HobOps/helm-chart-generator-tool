# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FakeFile
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.file_management.file_writer import YamlFileWriter
from base.infrastructure.path_management.path_handler import FakePath
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.file_management.file_constants import file_type_values


def test_yaml_file_writer_validation():
    """
    test_yaml_file_writer_validation
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

    fake_path = FakePath(fake_file=fake_file)
    path_handler = PathHandler(path_obj=fake_path)

    file_handler = FileHandler(file_obj=fake_file)

    yaml_file_writer = YamlFileWriter(path_handler=path_handler, file_handler=file_handler)
    yaml_file_writer.write_file(data=data)

    assert fake_file.content == expected_content
