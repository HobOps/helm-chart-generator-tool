# -*- coding: utf-8 -*-


from framework.base.domain.common.value_objects import BaseValueObject


class StringValueObject(BaseValueObject):
    """
    StringValueObject
    """

    def __init__(self, value: str):
        """
        StringValueObject constructor
        """

        self.__value = value

        if not self.is_valid():
            raise ValueError(f"Error value: {value} is not a str type")

    def is_valid(self):
        """
        is_valid
        @return:
        @rtype:
        """

        return isinstance(self.__value, str)

    @property
    def value(self) -> str:
        """
        value
        @return: value
        @rtype: str
        """

        return self.__value

