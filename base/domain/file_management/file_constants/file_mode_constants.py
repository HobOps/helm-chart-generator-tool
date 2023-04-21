# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass(frozen=True)
class FileModeValues:
    read: str
    write: str


file_mode_values = FileModeValues(read='r', write='w')
