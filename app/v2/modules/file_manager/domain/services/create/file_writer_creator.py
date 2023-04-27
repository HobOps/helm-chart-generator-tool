# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


# Domain
from base.domain.file_management.file_writer import BaseFileWriter


@runtime_checkable
class FileWriterCreator(Protocol):
    """
    FileWriterCreator
    """

    @abstractmethod
    def create_file_writer(self, file_type: str) -> BaseFileWriter:
        """
        create_writer
        @param file_type: file_type
        @type file_type: str
        @return: BaseFileWriter
        @rtype: BaseFileWriter
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")


