# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseDataHandler(Protocol):
    """
    BaseDataHandler
    """

    @abstractmethod
    def process(self, input_data: dict):
        """
        process
        @param input_data: input_data
        @type input_data: dict
        @return: output_data
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
