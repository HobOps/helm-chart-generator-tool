# -*- coding: utf-8 -*-


class ScriptHostAliasesReaderService:
    """
    ScriptHostAliasesReaderService
    """

    @staticmethod
    def read_host_aliases(host_aliases):
        result = list()
        if type(host_aliases) is list:
            for item in host_aliases:
                result.append(dict(
                    ip=item.ip,
                    hostnames=item.hostnames,
                ))
        return result
