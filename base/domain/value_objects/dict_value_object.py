# -*- coding: utf-8 -*-


from base.domain.value_objects import ValueObjectBase


class DictValueObject(ValueObjectBase):
    """
    DictValueObject
    """

    def __init__(self, value: dict):
        """
        DictValueObject constructor
        """

        self.__value = value

        if not self.__is_valid():
            raise ValueError(f"Error value: {value} is not a dict type")

    def __is_valid(self):
        """
        is_valid
        @return:
        @rtype:
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

