# -*- coding: utf-8 -*-


# Application
from app.v1.modules.kubernetes_services import ScriptToDictParserService


class ScriptEnvironReaderFromService:
    """
    ScriptEnvironReaderFromService
    """

    @staticmethod
    def read_env_from(items):
        env_from = list()
        if type(items) is list:
            for item in items:
                env_from.append(dict(
                    configMapRef=ScriptToDictParserService.to_dict(item.config_map_ref),
                    secretRef=ScriptToDictParserService.to_dict(item.secret_ref),
                    prefix=item.prefix
                ))
        return env_from
