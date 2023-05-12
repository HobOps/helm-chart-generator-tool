# -*- coding: utf-8 -*-


from app.v1.modules.file_manager import ScriptFileWriterManager


class ScriptHelmChartCreator:
    """
    ScriptHelmChartCreator
    """

    @staticmethod
    def create_chart_file(conf):
        # Render Chart maintainers
        maintainers = list()
        for item in conf['chart']['maintainers']:
            maintainers.append(dict(name=item))
        conf['chart']['maintainers'] = maintainers

        # Render dependencies
        conf['chart']['dependencies'] = [dict(
            name=conf['chart']['baseChartName'],
            version=conf['chart']['baseChartVersion'],
            repository=conf['chart']['baseChartRepository'],
        )]
        # Remove unnecessary keys from dictionary
        for item in ['baseChartVersion', 'baseChartName', 'baseChartRepository']:
            conf['chart'].pop(item)

        ScriptFileWriterManager.write_file(f"config_files/output/charts/{conf['chart']['name']}/Chart.yaml", conf['chart'])
        pass
