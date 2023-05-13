# -*- coding: utf-8 -*-


class ScriptImagePullSecretsReaderService:
    """
    ScriptImagePullSecretsReaderService
    """

    @staticmethod
    def read_image_pull_secrets(image_pull_secrets):
        result = list()
        if type(image_pull_secrets) is list:
            for item in image_pull_secrets:
                result.append(dict(
                    name=item.name
                ))
        return result
