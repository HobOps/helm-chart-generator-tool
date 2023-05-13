# -*- coding: utf-8 -*-


from kubernetes import config


class ScriptKubernetesConfigLoader:
    """
    ScriptKubernetesConfigLoader
    """

    @staticmethod
    def load_kubernetes_config(config_settings):
        contexts, active_context = config.list_kube_config_contexts()
        if not contexts:
            print("Cannot find any context in kube-config file.")
            exit(1)
        return config.load_kube_config(context=config_settings['kubernetes']['context'])
