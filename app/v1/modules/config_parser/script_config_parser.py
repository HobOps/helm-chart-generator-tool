# -*- coding: utf-8 -*-


def convert_values(value):
    values = dict(
        configmap='ConfigMap',
        secret='Secret',
        deployment='Deployment',
        statefulset='StatefulSet',
        ingress='Ingress',
        job='Job'
    )
    return values[value]


def parse_config_list(config_list):
    import re
    result = list()
    for item in re.split('[, \n]', config_list):
        if item != '':
            result.append(item)
    return result


class ScriptConfigParser:
    """
    ScriptConfigParser
    """

    @staticmethod
    def parse_config(component_name):
        """
        parse_config
        @param component_name: component_name
        @type component_name: str
        @return: result
        @rtype: dict
        """

        # Open config file
        import configparser
        import os.path

        config_path = f'config_files/input/configurations/{component_name}.ini'
        chart_config = configparser.ConfigParser()
        if os.path.isfile(config_path):
            chart_config.read(config_path)
        else:
            print(f'The configuration file {config_path} does not exist.')
            exit(1)

        # Parse config file
        result = dict()
        for section in chart_config:
            result[section] = dict()
            if section == 'kubernetes':
                result[section]['context'] = chart_config[section]['context']
                result[section]['namespace'] = chart_config[section]['namespace']
            elif section == 'flags':
                result[section]['remove_ingress_suffix'] = chart_config[section]['remove_ingress_suffix']
            elif section == 'chart':
                result[section]['apiVersion'] = chart_config[section]['apiVersion']
                result[section]['name'] = chart_config[section]['name']
                result[section]['description'] = chart_config[section]['description']
                result[section]['type'] = chart_config[section]['type']
                result[section]['version'] = chart_config[section]['version']
                result[section]['appVersion'] = chart_config[section]['appVersion']
                result[section]['maintainers'] = parse_config_list(chart_config[section]['maintainers'])
                result[section]['sources'] = parse_config_list(chart_config[section]['sources'])
                result[section]['baseChartVersion'] = chart_config[section]['baseChartVersion']
                result[section]['baseChartName'] = chart_config[section]['baseChartName']
                result[section]['baseChartRepository'] = chart_config[section]['baseChartRepository']
            elif section == 'components':
                for kind in chart_config[section]:
                    result[section][convert_values(kind)] = list()
                    result[section][convert_values(kind)] = parse_config_list(chart_config[section][kind])
            else:
                result.pop(section)
        return result
