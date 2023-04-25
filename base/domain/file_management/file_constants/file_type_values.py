# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass(frozen=True)
class FileTypeValues:
    """
    FileTypeValues
    """

    ini: str
    json: str
    text: str
    yaml: str


file_type_values = FileTypeValues(
    ini=".ini",
    json=".json",
    text=".txt",
    yaml=".yaml"
)

