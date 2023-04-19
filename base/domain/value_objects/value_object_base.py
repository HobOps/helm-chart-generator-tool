# -*- coding: utf-8 -*-


from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class ValueObjectBase(Protocol):
    """
    ValueObjectBase
    """

    def __init__(self):
        """
        ValueObjectBase constructor
        """

        raise NotImplementedError("Interface Missing Implementation")

    def is_valid(self):
        """
        is_valid
        @return: True
        @rtype: bool
        """

        raise NotImplementedError("Interface Missing Implementation")
    