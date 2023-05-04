# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseConfigReader(Protocol):
    """
    BaseConfigReader
    """

    @abstractmethod
    def read_configuration(self):
        """
        read_config_file
        @return: config_data
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

