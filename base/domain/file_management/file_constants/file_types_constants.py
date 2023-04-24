# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass(frozen=True)
class FileTypesValues:
    yaml: str
    json: str
    text: str


file_types_values = FileTypesValues(
    yaml="yaml",
    json="json",
    text="txt",
)
