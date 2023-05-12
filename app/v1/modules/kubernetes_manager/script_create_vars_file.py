# -*- coding: utf-8 -*-


# Application
from app.v1.modules.file_manager import ScriptFileWriterManager
from app.v1.modules.util_manager import ScriptUtilDictCleaner


class ScriptCreateVarsFile:
    """
    ScriptCreateVarsFile
    """

    @staticmethod
    def create_vars_file(conf):
        field = dict(
            ConfigMap='data',
            Secret='stringData'
        )
        for kind in conf['kubernetes']['values']:
            if kind in ['ConfigMap', 'Secret']:
                for item in conf['kubernetes']['values'][kind]:
                    ScriptFileWriterManager.write_file(
                        f"config_files/output/vars/{conf['chart']['name']}/{item}.json",
                        ScriptUtilDictCleaner.remove_empty_from_dict(conf['kubernetes']['values'][kind][item][field[kind]]),
                        mode='json'
                    )
        pass
