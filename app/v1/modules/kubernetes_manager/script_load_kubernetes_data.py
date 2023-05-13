# -*- coding: utf-8 -*-


from kubernetes import client

# Application
from app.v1.modules.kubernetes_manager import ScriptConfigMapSecretCreator
from app.v1.modules.kubernetes_manager import ScriptIngressCreator
from app.v1.modules.kubernetes_manager import ScriptWorkloadCreator


class ScriptKubernetesDataLoader:
    """
    ScriptKubernetesDataLoader
    """

    @staticmethod
    def load_kubernetes_data(conf):
        conf['kubernetes']['values'] = dict()
        for kind in conf['components'].keys():
            print("==== " + kind)
            values = dict()
            if kind in ['ConfigMap', 'Secret']:
                for component in conf['components'][kind]:
                    values[component] = ScriptConfigMapSecretCreator.create_configmap_or_secret(
                        kind=kind,
                        name=component,
                        k8s_client=client,
                        namespace=conf['kubernetes']['namespace']
                    )
                    pass
            elif kind in ['Job', 'Deployment', 'StatefulSet']:
                for component in conf['components'][kind]:
                    values[component] = ScriptWorkloadCreator.create_workload(
                        kind=kind,
                        name=component,
                        k8s_client=client,
                        namespace=conf['kubernetes']['namespace']
                    )
                    pass
            elif kind == 'Ingress':
                try:
                    name_suffix = conf['flags']['remove_ingress_suffix']
                except KeyError:
                    name_suffix = ''
                for component in conf['components'][kind]:
                    values[component] = ScriptIngressCreator.create_ingress(
                        name=component,
                        name_suffix=name_suffix,
                        k8s_client=client,
                        namespace=conf['kubernetes']['namespace'],
                    )
                    pass
            conf['kubernetes']['values'][kind] = values
        pass

