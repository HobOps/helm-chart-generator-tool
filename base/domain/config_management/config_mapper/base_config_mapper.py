# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseConfigMapper(Protocol):
    """
    BaseConfigMapper
    """

    @staticmethod
    @abstractmethod
    def map_config_data(config_parser):
        """
        map_config_data
        @param config_parser: config_parser
        @type config_parser: configparser
        @return: config_data
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

