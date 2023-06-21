# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


from core.modules.data_manager import BaseDataHandler


@runtime_checkable
class BaseDataPipeline(Protocol):
    """
    BaseDataPipeline
    """

    @abstractmethod
    def add_handler(self, data_handler: BaseDataHandler):
        """
        add_handler
        @param data_handler: data_handler
        @type data_handler: BaseDataHandler
        @return: data_pipeline
        @rtype: BaseDataPipeline
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    def execute(self, input_data: dict):
        """
        execute
        @param input_data: input_data
        @type input_data: dict
        @return: output_data
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
