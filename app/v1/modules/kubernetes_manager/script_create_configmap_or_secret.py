# -*- coding: utf-8 -*-


class ScriptConfigMapSecretCreator:
    """
    ConfigMapSecretCreator
    """

    @staticmethod
    def create_configmap_or_secret(kind, name, k8s_client, namespace):
        import base64
        v1 = k8s_client.CoreV1Api()
        result = dict()
        print(name)
        ret = ''
        if kind == "ConfigMap":
            ret = v1.list_namespaced_config_map(
                field_selector="metadata.name={name}".format(name=name),
                namespace=namespace,
            )
            result['data'] = ret.items[0].data
        elif kind == "Secret":
            ret = v1.list_namespaced_secret(
                field_selector="metadata.name={name}".format(name=name),
                namespace=namespace,
            )
            string_data = dict()
            for item in ret.items[0].data:
                string_data[item] = base64.b64decode(ret.items[0].data[item]).decode("utf-8")
            result['stringData'] = string_data
        return result

