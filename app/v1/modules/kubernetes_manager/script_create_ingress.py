# -*- coding: utf-8 -*-


# Application
from app.v1.modules.kubernetes_services import ScriptAnnotationsReaderService
from app.v1.modules.kubernetes_services import ScriptIngressRulesReaderService
from app.v1.modules.kubernetes_services import ScriptIngressTlsReaderService


class ScriptIngressCreator:
    """
    ScriptIngressCreator
    """

    @staticmethod
    def create_ingress(name: str, k8s_client, namespace, name_suffix=''):
        ingress_name = name.replace(name_suffix, '')
        v1 = k8s_client.NetworkingV1Api()
        ret = v1.list_namespaced_ingress(
            field_selector="metadata.name={name}".format(name=ingress_name),
            namespace=namespace
        )
        print(ingress_name)
        return dict(
            annotations=ScriptAnnotationsReaderService.read_annotations(ret.items[0].metadata.annotations),
            rules=ScriptIngressRulesReaderService.read_ingress_rules(ret.items[0].spec.rules),
            tls=ScriptIngressTlsReaderService.read_ingress_tls(ret.items[0].spec.tls)
        )
