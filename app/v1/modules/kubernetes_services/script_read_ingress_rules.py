# -*- coding: utf-8 -*-


class ScriptIngressRulesReaderService:
    """
    ScriptIngressRulesReaderService
    """

    @staticmethod
    def read_ingress_rules(rules):
        result = list()
        for item in rules:
            rule = dict()
            rule['host'] = item.host
            rule['http'] = dict(
                paths=list()
            )
            for path in item.http.paths:
                rule['http']['paths'].append(dict(
                    path=path.path,
                    backend=path.backend.to_dict(),
                    pathType=path.path_type
                ))
            result.append(rule)
        return result
