# -*- coding: utf-8 -*-


from core.modules.data_management.base_data_handler import BaseDataHandler


class DummyValuesExtractDataFilter(BaseDataHandler):
    """
    DummyValuesExtractDataFilter
    """

    def __init__(self, config_data: str):
        """
        DummyValuesExtractDataFilter constructor
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

        output_data = dict()

        for item in input_data:
            if item == self.__config_data:
                output_data.update({item: input_data[item]})

        return output_data
