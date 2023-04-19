# -*- coding: utf-8 -*-


from typing import Protocol
from typing import runtime_checkable
from abc import abstractmethod


@runtime_checkable
class BaseValueObject(Protocol):
    """
    BaseValueObject
    """

    @abstractmethod
    def __is_valid(self):
        """
        is_valid
        @return: True
        @rtype: bool
        """

        raise NotImplementedError("Interface Missing Implementation")

    @property
    @abstractmethod
    def value(self):
        """
        value
        @return: value
        @rtype: Any
        """

        raise NotImplementedError("Interface Missing Implementation")
