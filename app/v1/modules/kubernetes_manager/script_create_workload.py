# -*- coding: utf-8 -*-


# Application
from app.v1.modules.kubernetes_manager import ScriptWorkloadTemplateCreator


class ScriptWorkloadCreator:
    """
    ScriptWorkloadCreator
    """

    @staticmethod
    def create_workload(kind, name, k8s_client, namespace):
        v1 = k8s_client.AppsV1Api()
        result = dict()
        print(name)
        ret = ''
        if kind == "Job":
            v1 = k8s_client.BatchV1Api()
            ret = v1.list_namespaced_job(
                field_selector="metadata.name={name}".format(name=name),
                namespace=namespace
            )
        elif kind == "StatefulSet":
            ret = v1.list_namespaced_stateful_set(
                field_selector="metadata.name={name}".format(name=name),
                namespace=namespace
            )
            result = result | dict(replicas=ret.items[0].spec.replicas)
        elif kind == "Deployment":
            ret = v1.list_namespaced_deployment(
                field_selector="metadata.name={name}".format(name=name),
                namespace=namespace
            )
            result = result | dict(replicas=ret.items[0].spec.replicas)
        return result | ScriptWorkloadTemplateCreator.create_workload_template(ret, name)
