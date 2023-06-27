# -*- coding: utf-8 -*-


from copy import deepcopy


from core.modules.data_management import BaseDataHandler
from core.modules.data_management import BaseDataPipeline


class HelmDeploymentVarsDataProcessing(BaseDataPipeline):
    """
    HelmDeploymentVarsDataProcessing
    """

    def __init__(self):
        """
        HelmDeploymentVarsDataProcessing constructor
        """

        self.__data_handlers = []

    def add_handler(self, data_handler: BaseDataHandler):
        """
        add_handler
        @param data_handler: data_handler
        @type data_handler: BaseDataHandler
        @return: self
        @rtype: BaseDataPipeline
        """

        self.__data_handlers.append(data_handler)

        return self

    def execute(self, input_data: dict):
        """
        execute
        @param input_data: input_data
        @type input_data: dict
        @return: output_data
        @rtype: dict
        """

        output_data = deepcopy(input_data)

        for data_handler in self.__data_handlers:
            output_data = data_handler.process(output_data)

        return output_data
