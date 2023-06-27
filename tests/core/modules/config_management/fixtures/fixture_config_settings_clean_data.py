# -*- coding: utf-8 -*-


import pytest


# -------------------------------
# Fixture for testings purposes
# Based on current k3s01 config
# -------------------------------

@pytest.fixture()
def fixture_config_settings_clean_data():
    """
    fixture_config_settings_clean_data
    @return: config_settings_clean_fixture
    @rtype: dict
    """

    config_settings_clean_fixture = {
        'chart': {
            'apiVersion': 'v2',
            'appVersion': '1.16.0',
            'dependencies': [
                {
                    'name': 'common-library',
                    'repository': 'https://hobops-helm-charts.storage.googleapis.com',
                    'version': '1.0.11'
                }
            ],
            'description': 'A '
                           'Helm '
                           'chart '
                           'for '
                           'Kubernetes',
            'maintainers': [
                {
                    'name': 'DevOps'
                }
            ],
            'name': 'k3s01',
            'sources': ['https://example.com/test'],
            'type': 'application',
            'version': '0.1.0'
        },
        'components': {
            'ConfigMap': [
                'example-html'
            ],
            'Deployment': [
                'nginx-deployment',
                'my-nginx-deployment'
            ],
            'Ingress': [
                'nginx-deployment'
            ],
            'StatefulSet': [
                'web-statefulset'
            ]
        },
        'kubernetes': {
            'context': 'k3s01',
            'namespace': 'default',
            'values': {
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
                                'name': 'FOO_VARIABLE1',
                                'value': '123',
                            },
                            {
                                'name': 'FOO_VARIABLE2',
                                'value': '$(FOO_VARIABLE1)',
                            },
                            {
                                'name': 'FOO_VARIABLE3',
                                'value': 'host_name_example2',
                            },
                            {
                                'name': 'FOO_VARIABLE4',
                                'value': '$(FOO_VARIABLE3)',
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
                                'name': 'html-volume',
                            }
                        ],
                        'volumes': [
                            {
                                'configMap':
                                    {
                                        'defaultMode': 420,
                                        'name': 'example-html',
                                    },
                                'name': 'html-volume',
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
                        ],
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
    }

    return config_settings_clean_fixture
