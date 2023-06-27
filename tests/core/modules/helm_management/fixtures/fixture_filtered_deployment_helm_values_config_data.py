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
                'my-nginx-deployment': {
                    'image': {
                        'repository': 'redis',
                        'tag': 'latest'
                    },
                    'replicas': 1,
                    'selectorLabels': {
                        'app': 'my-nginx-deployment'
                    },
                    'service': {
                        'ports': [
                            {
                                'port': 8080,
                                'protocol': 'TCP'
                            }
                        ]
                    },
                },
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
            },
            'StatefulSet': {
                'web-statefulset': {
                    'env': [
                        {
                            'name': 'FOO_VARIABLE5',
                            'value': '456',
                        },
                        {
                            'name': 'FOO_VARIABLE6',
                            'value': '$(FOO_VARIABLE5)',
                        },
                        {
                            'name': 'FOO_VARIABLE7',
                            'value': 'host_name_example3',
                        },
                        {
                            'name': 'FOO_VARIABLE8',
                            'value': '$(FOO_VARIABLE7)',
                        }
                    ],
                    'image': {
                        'repository': 'registry.k8s.io/nginx-slim',
                        'tag': '0.8'
                    },
                    'replicas': 2,
                    'selectorLabels': {
                        'app': 'web-statefulset'
                    },
                    'service': {
                        'ports': [
                            {
                                'name': 'web-statefulset',
                                'port': 80,
                                'protocol': 'TCP'
                            }
                        ]
                    },
                    'volumeMounts': [
                        {
                            'mountPath': '/usr/share/nginx/html',
                            'name': 'www',
                        }
                    ],
                }
            }
        }
    }

    return filtered_deployment_helm_values_config_data
