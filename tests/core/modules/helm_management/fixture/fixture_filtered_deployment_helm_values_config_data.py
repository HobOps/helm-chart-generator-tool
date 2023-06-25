# -*- coding: utf-8 -*-


import pytest


@pytest.fixture
def fixture_filtered_deployment_helm_values_config_data():
    """
    fixture_filtered_deployment_helm_values_config_data
    @return: filtered_deployment_helm_values_config_data
    @rtype: dict
    """

    filtered_deployment_helm_values_config_data = {
        'common-library': {
            'ConfigMap': {
                'example-html': {
                    'data': {
                        'index.html': '<!DOCTYPE '
                        'html>\n'
                        '<html>\n'
                        '<head>\n'
                        '  '
                        '<title>Example '
                        'HTML '
                        'Page</title>\n'
                        '</head>\n'
                        '<body>\n'
                        '  '
                        '<h1>Welcome '
                        'to '
                        'the '
                        'Example '
                        'HTML '
                        'Page!</h1>\n'
                        '  '
                        '<p>This '
                        'is '
                        'an '
                        'example '
                        'HTML '
                        'page '
                        'that '
                        'will '
                        'be '
                        'mounted '
                        'as '
                        'the '
                        'default '
                        'page '
                        'in '
                        'an '
                        'Nginx '
                        'container.</p>\n'
                        '</body>\n'
                        '</html>\n'}}},
            'Deployment': {
                'nginx-deployment': {
                    'env': [
                        {
                            'name': 'FOO_VARIABLE2',
                            'value': '$(FOO_VARIABLE1)'
                        },
                        {
                            'name': 'FOO_VARIABLE4',
                            'value': '$(FOO_VARIABLE3)'
                        }
                    ],
                    'image': {
                        'repository': 'nginx',
                        'tag': 'latest'
                    },
                    'replicas': 4,
                    'selectorLabels': {
                        'app': 'nginx-deployment'
                    },
                    'service': {
                        'ports': [
                            {
                                'port': 80,
                                'protocol': 'TCP'
                            }
                        ]
                    },
                    'volumeMounts': [
                        {
                            'mountPath': '/usr/share/nginx/html',
                            'name': 'html-volume'
                        }
                    ],
                    'volumes': [
                        {
                            'configMap': {
                                'defaultMode': 420,
                                'name': 'example-html'
                            },
                            'name': 'html-volume'
                        }
                    ]
                }
            },
            'Ingress': {
                'nginx-deployment': {
                    'rules': [
                        {
                            'host': 'k3s01.dc4.infra.hobops.io',
                            'http': {
                                'paths': [
                                    {
                                        'backend': {
                                            'service': {
                                                'name': 'nginx-deployment',
                                                'port': {
                                                    'number': 80
                                                }
                                            }
                                        },
                                        'path': '/',
                                        'pathType': 'Prefix'
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

    return filtered_deployment_helm_values_config_data
