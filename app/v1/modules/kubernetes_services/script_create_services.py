# -+- coding: utf-8 -*-


class ScriptServicesCreatorService:
    """
    ScriptServicesCreatorService
    """

    @staticmethod
    def create_services(services):
        result = list()
        if type(services) is list:
            for service in services:
                result.append(dict(
                    name=service.name,
                    port=service.container_port,
                    hostIp=service.host_ip,
                    hostPort=service.host_port,
                    protocol=service.protocol
                ))
        return result

