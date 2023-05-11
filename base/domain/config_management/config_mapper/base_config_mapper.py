# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseConfigMapper(Protocol):
    """
    BaseConfigMapper
    """

    @abstractmethod
    def map_config_data(self):
        """
        map_config_data
        @return: config_data
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

