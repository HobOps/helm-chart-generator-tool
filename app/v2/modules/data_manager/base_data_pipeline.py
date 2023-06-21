# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


from app.v2.modules.data_manager import BaseDataFilter


@runtime_checkable
class BaseDataPipeline(Protocol):
    """
    BaseDataPipeline
    """

    @abstractmethod
    def add_filter(self, data_filter: BaseDataFilter):
        """
        add_filter
        @param data_filter: data_filter
        @type data_filter: BaseDataFilter
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
