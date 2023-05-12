# -*- coding: utf-8 -*-


import os


# Application
from app.v1.modules.kubernetes_services import ScriptToDictParserService


class ScriptEnvironReaderService:
    """
    ScriptEnvironReaderService
    """

    @staticmethod
    def read_env(items):
        variables_to_remove = [
            'FOO'
        ]
        # TODO: Refactor this section
        prefixes_to_remove = [
            'STAKATER_',
        ]
        env = list()
        if type(items) is list:
            for item in items:
                # Remove variables based on prefixes_to_remove
                if os.path.commonprefix([prefixes_to_remove[0], item.name]) == prefixes_to_remove[0]:
                    continue
                elif item.name in variables_to_remove:
                    continue
                env.append(dict(
                    name=item.name,
                    value=item.value,
                    valueFrom=ScriptToDictParserService.to_dict(item.value_from)
                ))
        return env
