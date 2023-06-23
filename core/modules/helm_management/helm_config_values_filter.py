# -*- coding: utf-8 -*-


# Domain
from core.modules.data_management import BaseDataHandler


class HelmConfigValuesFilter(BaseDataHandler):
    """
    HelmConfigValuesFilter
    """

    def process(self, conf: dict):
        """
        process
        @param conf: conf
        @type conf: dict
        @return: values
        @rtype: dict
        """

        if not isinstance(conf, dict):
            raise ValueError(f"Error conf: {conf} is not dict type")

        values = dict()
        values['common-library'] = dict()

        for kind in conf['kubernetes']['values']:
            values['common-library'][kind] = dict()
            for item in conf['kubernetes']['values'][kind]:
                values['common-library'][kind][item] = conf['kubernetes']['values'][kind][item]

        return values
