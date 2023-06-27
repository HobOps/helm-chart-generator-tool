# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentData:
    """
    ArgumentData
    """

    name: str
    version: str
