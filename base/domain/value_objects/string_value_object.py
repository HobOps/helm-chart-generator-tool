# -*- coding: utf-8 -*-


from base.domain.value_objects import BaseValueObject


class StringValueObject(BaseValueObject):
    """
    StringValueObject
    """

    def __init__(self, value: str):
        """
        StringValueObject constructor
        """

        self.__value = value

        if not self.__is_valid():
            raise ValueError(f"Error value: {value} is not a str type")

    def __is_valid(self):
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

