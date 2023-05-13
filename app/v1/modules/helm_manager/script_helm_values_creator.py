# -*- coding: utf-8 -*-


from app.v1.modules.file_manager import ScriptFileWriterManager
from app.v1.modules.utility_services import ScriptUtilDictCleaner


class ScriptHelmValuesCreator:
    """
    ScriptHelmValuesCreator
    """

    @staticmethod
    def create_values_file(conf):
        values = dict()
        values['common-library'] = dict()
        for kind in conf['kubernetes']['values']:
            values['common-library'][kind] = dict()
            for item in conf['kubernetes']['values'][kind]:
                values['common-library'][kind][item] = conf['kubernetes']['values'][kind][item]
                # Remove variables from "values.yaml" file
                # if kind == 'ConfigMap':
                #     values['common-library'][kind][item]['data'] = {}
                # elif kind == 'Secret':
                #     values['common-library'][kind][item]['data'] = {}
                #     values['common-library'][kind][item]['stringData'] = {}
        ScriptFileWriterManager.write_file(
            f"config_files/output/charts/{conf['chart']['name']}/values.yaml",
            ScriptUtilDictCleaner.remove_empty_from_dict(values),
        )
        pass
