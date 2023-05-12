# -*- coding: utf-8 -*-


class ScriptAnnotationsReaderservice:
    """
    ScriptAnnotationsReaderservice
    """

    @staticmethod
    def read_annotations(annotations: dict):
        result = annotations
        annotations_to_remove = [
            'deployment.kubernetes.io/revision',
            'field.cattle.io/publicEndpoints',
            'meta.helm.sh/release-name',
            'meta.helm.sh/release-namespace',
            'objectset.rio.cattle.io/applied',
            'objectset.rio.cattle.io/id',
            'kubectl.kubernetes.io/last-applied-configuration',
            'kubernetes.io/change-cause',
        ]
        for item in annotations_to_remove:
            result.pop(item, None)
        return result
