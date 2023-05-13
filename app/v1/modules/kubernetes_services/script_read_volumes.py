# -*- coding: utf-8 -*-


# Application
from app.v1.modules.kubernetes_services import ScriptToDictParserService


class ScriptVolumesReaderService:
    """
    ScriptVolumesReaderService
    """

    @staticmethod
    def read_volumes(items):
        values = list()
        if type(items) is list:
            for item in items:
                values.append(dict(
                    name=item.name,
                    configMap=ScriptToDictParserService.to_dict(item.config_map),
                    secret=ScriptToDictParserService.to_dict(item.secret),
                    hostPath=ScriptToDictParserService.to_dict(item.host_path)
                ))
        return values
