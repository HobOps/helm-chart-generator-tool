# -*- coding: utf-8 -*-


from copy import deepcopy

from core.modules.data_management.base_data_handler import BaseDataHandler


class DummyValuesRemoveDataFilter(BaseDataHandler):
    """
    DummyValuesRemoveDataFilter
    """

    def __init__(self, config_data: str):
        """
        DummyValuesRemoveDataFilter
        @param config_data: config_data
        @type config_data: str
        """

        self.__config_data = config_data

    def process(self, input_data: dict):
        """
        process
        @param input_data: input_data
        @type input_data: dict
        @return: output_data
        @rtype: dict
        """

        output_data = deepcopy(input_data["valid_key"])

        for item in input_data["valid_key"]:
            if item == self.__config_data:
                output_data.pop(item)

        return output_data
