# -*- coding: utf-8 -*-


class ScriptVolumeMountsReaderService:
    """
    ScriptVolumeMountsReaderService
    """

    @staticmethod
    def read_volume_mounts(items):
        values = list()
        if type(items) is list:
            for item in items:
                values.append(dict(
                    mountPath=item.mount_path,
                    mountPropagation=item.mount_propagation,
                    name=item.name,
                    readOnly=item.read_only,
                    subPath=item.sub_path,
                    subPathExpr=item.sub_path_expr
                ))
        return values
