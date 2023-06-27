# -*- coding: utf-8 -*-


from framework.base.domain.common.value_objects import BaseValueObject


class ListValueObject(BaseValueObject):
    """
    ListValueObject
    """

    def __init__(self, value: list):
        """
        ListValueObject constructor
        """

        self.__value = value

        if not self.is_valid():
            raise ValueError(f"Error value: {value} is not a list type")

    def is_valid(self):
        """
        is_valid
        @return: True
        @rtype: bool
        """

        return isinstance(self.__value, list)

    @property
    def value(self) -> list:
        """
        value
        @return: value
        @rtype: list
        """

        return self.__value

