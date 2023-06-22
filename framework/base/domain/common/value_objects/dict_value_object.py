# -*- coding: utf-8 -*-


from framework.base.domain.common.value_objects import BaseValueObject


class DictValueObject(BaseValueObject):
    """
    DictValueObject
    """

    def __init__(self, value: dict):
        """
        DictValueObject constructor
        """

        self.__value = value

        if not self.is_valid():
            raise ValueError(f"Error value: {value} is not a dict type")

    def is_valid(self):
        """
        is_valid
        @return: True
        @rtype: bool
        """

        return isinstance(self.__value, dict)

    @property
    def value(self) -> dict:
        """
        value
        @return: value
        @rtype: dict
        """

        return self.__value

