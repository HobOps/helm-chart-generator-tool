# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FakeFile
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.file_management.file_writer import TextFileWriter
from base.infrastructure.path_management.path_handler import FakePath
from base.infrastructure.path_management.path_handler import PathHandler

# Domain
from base.domain.file_management.file_constants import file_type_values


def test_text_file_writer_validation():
    """
    test_text_file_writer_validation
    """

    data = [
        "data1",
        "data2",
        "data3",
        "data4",
    ]

    fake_file = FakeFile(file_name="fake_file_tester", file_type_suffix=file_type_values.text)
    fake_file.open()

    fake_path = FakePath(fake_file=fake_file)
    path_handler = PathHandler(path_obj=fake_path)

    file_handler = FileHandler(file_obj=fake_file)

    text_file_writer = TextFileWriter(path_handler=path_handler, file_handler=file_handler)
    text_file_writer.write_file(data=data)

    assert fake_file.content == '\n'.join(data)

