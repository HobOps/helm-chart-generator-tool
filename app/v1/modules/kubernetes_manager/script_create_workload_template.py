# -*- coding: utf-8 -*-


# Application
from app.v1.modules.kubernetes_services import ScriptAnnotationsReaderService
from app.v1.modules.kubernetes_services import ScriptEnvironReaderService
from app.v1.modules.kubernetes_services import ScriptEnvironReaderFromService
from app.v1.modules.kubernetes_services import ScriptHostAliasesReaderService
from app.v1.modules.kubernetes_services import ScriptImagePullSecretsReaderService
from app.v1.modules.kubernetes_services import ScriptServicesCreatorService
from app.v1.modules.kubernetes_services import ScriptToDictParserService
from app.v1.modules.kubernetes_services import ScriptVolumesReaderService
from app.v1.modules.kubernetes_services import ScriptVolumeMountsReaderService


class ScriptWorkloadTemplateCreator:
    """
    ScriptWorkloadTemplateCreator
    """

    @staticmethod
    def create_workload_template(ret, name):
        return dict(
            annotations=ScriptAnnotationsReaderService.read_annotations(ret.items[0].metadata.annotations),
            selectorLabels=dict(
                app=name
            ),
            image=dict(
                repository=ret.items[0].spec.template.spec.containers[0].image.split(':')[0],
                tag=ret.items[0].spec.template.spec.containers[0].image.split(':')[1]
            ),
            command=ret.items[0].spec.template.spec.containers[0].command,
            args=ret.items[0].spec.template.spec.containers[0].args,
            env=ScriptEnvironReaderService.read_env(ret.items[0].spec.template.spec.containers[0].env),
            envFrom=ScriptEnvironReaderFromService.read_env_from(ret.items[0].spec.template.spec.containers[0].env_from),
            service=dict(
                ports=ScriptServicesCreatorService.create_services(ret.items[0].spec.template.spec.containers[0].ports)
            ),
            volumes=ScriptVolumesReaderService.read_volumes(ret.items[0].spec.template.spec.volumes),
            volumeMounts=ScriptVolumeMountsReaderService.read_volume_mounts(ret.items[0].spec.template.spec.containers[0].volume_mounts),
            serviceAccount=(ret.items[0].spec.template.spec.service_account, None)[
                ret.items[0].spec.template.spec.service_account == 'default'
            ],
            imagePullSecrets=ScriptImagePullSecretsReaderService.read_image_pull_secrets(ret.items[0].spec.template.spec.image_pull_secrets),
            hostAliases=ScriptHostAliasesReaderService.read_host_aliases(ret.items[0].spec.template.spec.host_aliases),
            readinessProbe=ScriptToDictParserService.to_dict(ret.items[0].spec.template.spec.containers[0].readiness_probe),
            livenessProbe=ScriptToDictParserService.to_dict(ret.items[0].spec.template.spec.containers[0].liveness_probe),
            # TODO: Add missing resources
            # securityContext=to_dict(ret.items[0].spec.template.spec.containers[0].security_context),
            # strategy
            # resources
            # security_context
        )
