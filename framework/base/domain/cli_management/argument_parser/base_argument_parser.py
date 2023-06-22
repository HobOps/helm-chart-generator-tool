# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseArgumentParser(Protocol):
    """
    BaseArgumentParser
    """

    @abstractmethod
    def add_arguments(self, args_config: dict):
        """
        add_arguments
        @param args_config: args_config
        @type args_config: dict
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def parse_arguments(self):
        """
        parse_arguments
        @return: args
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
