# -*- coding: utf-8 -*-


from abc import abstractmethod
from configparser import ConfigParser
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseConfigReader(Protocol):
    """
    BaseConfigReader
    """

    @abstractmethod
    def get_config_parser(self) -> ConfigParser:
        """
        get_config_data
        @return: config_parser
        @rtype: ConfigParser
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

