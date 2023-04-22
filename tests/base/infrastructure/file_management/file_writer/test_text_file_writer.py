# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FakeFile
from base.infrastructure.file_management.file_handler import FileHandler
from base.infrastructure.file_management.file_writer import TextFileWriter
from base.infrastructure.path_management.path_handler import PathHandler


def test_text_file_writer_validation():
    """
    test_text_file_writer_validation
    """

    data = {
        "key1": "data1",
        "key2": "data2",
        "key3": {
            "key31": "data31",
            "key32": "data32"
        }
    }

    path_handler = PathHandler(current_path='/fake_root/fake_dir', expected_path='/fake_file')
    fake_file = FakeFile()
    fake_file.open()

    file_handler = FileHandler(file_obj=fake_file)

    text_file_writer = TextFileWriter(path_handler=path_handler, file_handler=file_handler)
    text_file_writer.write_file(data=data)

    assert fake_file.content is not None
    assert True

