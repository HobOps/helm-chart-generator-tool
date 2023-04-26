# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass(frozen=True)
class PathTypeValues:
    """
    PathTypeValues
    """

    directory: str
    file: str
    exec: str


path_types_values = PathTypeValues(
    directory="folder",
    file="file",
    exec="executable",
)
