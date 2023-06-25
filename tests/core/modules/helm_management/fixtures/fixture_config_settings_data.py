# -*- coding: utf-8 -*-


# Fixture for testings purposes
# Based on current k3s01 config


config_settings_fixture = {
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
        'sources': [   'https://example.com/test'],
        'type': 'application',
        'version': '0.1.0'
    },
    'components': {
        'ConfigMap': [
            'example-html'
        ],
        'Deployment': [
            'nginx-deployment'
        ],
        'Ingress': [
            'nginx-deployment'
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
                'nginx-deployment': {
                    'annotations': {   },
                    'args': None,
                    'command': None,
                    'env': [
                        {
                            'name': 'FOO_VARIABLE1',
                            'value': '123',
                            'valueFrom': None
                        },
                        {
                            'name': 'FOO_VARIABLE2',
                            'value': '$(FOO_VARIABLE1)',
                            'valueFrom': None
                        },
                        {
                            'name': 'FOO_VARIABLE3',
                            'value': 'host_name_example2',
                            'valueFrom': None
                        },
                        {
                            'name': 'FOO_VARIABLE4',
                            'value': '$(FOO_VARIABLE3)',
                            'valueFrom': None
                        }
                    ],
                    'envFrom': [   ],
                    'hostAliases': [   ],
                    'image': {
                        'repository': 'nginx',
                        'tag': 'latest'
                    },
                    'imagePullSecrets': [   ],
                    'livenessProbe': None,
                    'readinessProbe': None,
                    'replicas': 4,
                    'selectorLabels': {
                        'app': 'nginx-deployment'
                    },
                    'service': {
                        'ports': [
                            {
                                'hostIp': None,
                                'hostPort': None,
                                'name': None,
                                'port': 80,
                                'protocol': 'TCP'
                            }
                        ]
                    },
                    'serviceAccount': None,
                    'volumeMounts': [
                        {
                            'mountPath': '/usr/share/nginx/html',
                            'mountPropagation': None,
                            'name': 'html-volume',
                            'readOnly': None,
                            'subPath': None,
                            'subPathExpr': None
                        }
                    ],
                    'volumes': [
                        {
                            'configMap':
                                {
                                    'defaultMode': 420,
                                    'items': None,
                                    'name': 'example-html',
                                    'optional': None
                                },
                            'hostPath': None,
                            'name': 'html-volume',
                            'secret': None
                        }
                    ]
                }
            },
            'Ingress': {
                'nginx-deployment': {
                    'annotations': {   },
                    'rules': [
                        {
                            'host': 'k3s01.dc4.infra.hobops.io',
                            'http': {
                                'paths': [
                                    {
                                        'backend': {
                                            'resource': None,
                                            'service': {
                                                'name': 'nginx-deployment',
                                                'port': {
                                                    'name': None,
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
                    'tls': [   ]
                }
            }
        }
    }
}
