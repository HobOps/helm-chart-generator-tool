# -*- coding: utf-8 -*-


class ScriptIngressTlsReaderService:
    """
    ScriptIngressTlsReaderService
    """

    @staticmethod
    def read_ingress_tls(tls):
        result = list()
        if type(tls) is list:
            for item in tls:
                result.append(dict(
                    secretName=item.secret_name,
                    hosts=item.hosts
                ))
        return result

