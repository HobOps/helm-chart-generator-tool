# -*- coding: utf-8 -*-


# Application
from app.v1.modules.file_manager import ScriptFileWriterManager


class ScriptEnvironValuesFileCreator:
    """
    ScriptEnvironValuesFileCreator
    """

    @staticmethod
    def create_environment_values_file(conf):
        file = f"config_files/output/environments/{conf['chart']['name']}/{conf['chart']['name']}.values.yaml.gotmpl"
        data = list()
        data.append('# Load global and environment settings')
        data.append('{{ readFile "../../include/values.global.yaml" }}')
        data.append('{{ readFile "values.environment.yaml" }}')
        data.append('')
        for kind in conf['kubernetes']['values'].keys():
            if kind == 'ConfigMap':
                data.append(f'### {kind}')
                for component in conf['kubernetes']['values'][kind]:
                    data.append(f'{component}:')
                    data.append(f'  data: {{}}')
                    # Save variables to file
                    data.append(f'')
                    pass
            elif kind == 'Secret':
                data.append(f'### {kind}')
                for component in conf['kubernetes']['values'][kind]:
                    data.append(f'{component}:')
                    data.append(f'  stringData: {{}}')
                    data.append(f'')
                    pass
            elif kind in ['Deployment', 'StatefulSet']:
                data.append(f'### {kind}')
                for component in conf['kubernetes']['values'][kind]:
                    data.append(f'{component}:')
                    data.append(f'  <<: *default-environment')
                    data.append(f'  <<: *default-global-resources-nolimit')
                    data.append(f"  replicaCount: {conf['kubernetes']['values'][kind][component]['replicas']}")
                    data.append(f"  image:")
                    data.append(f"    repository: {conf['kubernetes']['values'][kind][component]['image']['repository']}")
                    data.append(f"    tag: {conf['kubernetes']['values'][kind][component]['image']['tag']}")
                    data.append(f'')
                    pass
            elif kind == 'Ingress':
                data.append(f'### {kind}')
                for component in conf['kubernetes']['values'][kind]:
                    data.append(f'{component}:')
                    if conf['kubernetes']['values'][kind][component]['annotations']:
                        data.append(f'  annotations:')
                        for key, value in conf['kubernetes']['values'][kind][component]['annotations'].items():
                            data.append(f"    {key}: {value}")
                    data.append(f"  host: {conf['kubernetes']['values'][kind][component]['rules'][0]['host']}")
                    pass
                data.append('')
        ScriptFileWriterManager.write_file(file, data, mode='raw')
        pass
