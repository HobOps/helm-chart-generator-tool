# -*- coding: utf-8 -*-


from kubernetes import client


class ScriptToDictParserService:
    """
    ScriptToDictParserService
    """

    @staticmethod
    def to_dict(item):
        if type(item) in [
            client.V1ConfigMapEnvSource,
            client.V1ContainerPort,
            client.V1EnvFromSource,
            client.V1EnvVarSource,
            client.V1SecretEnvSource,
            client.V1ConfigMapVolumeSource,
            client.V1SecretVolumeSource,
            client.V1VolumeMount,
            client.V1Probe
        ]:
            # This section converts dictionary keys from underscore to camel case
            values = item.to_dict()
            if type(item) is client.V1EnvVarSource:
                values['configMapKeyRef'] = values.pop('config_map_key_ref')
            elif type(item) is client.V1ConfigMapVolumeSource:
                values['defaultMode'] = values.pop('default_mode')
            elif type(item) is client.V1SecretVolumeSource:
                values['defaultMode'] = values.pop('default_mode')
                values['secretName'] = values.pop('secret_name')
            elif type(item) is client.V1Probe:
                values['failureThreshold'] = values.pop('failure_threshold')
                values['httpGet'] = values.pop('http_get')
                values['initialDelaySeconds'] = values.pop('initial_delay_seconds')
                values['periodSeconds'] = values.pop('period_seconds')
                values['successThreshold'] = values.pop('success_threshold')
                values['tcpSocket'] = values.pop('tcp_socket')
                values['terminationGracePeriodSeconds'] = values.pop('termination_grace_period_seconds')
                values['timeoutSeconds'] = values.pop('timeout_seconds')
            else:
                values = item.to_dict()
            return values
        else:
            return None
