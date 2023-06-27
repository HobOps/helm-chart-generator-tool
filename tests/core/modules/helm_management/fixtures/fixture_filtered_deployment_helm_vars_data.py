# -*- coding: utf-8 -*-


import pytest


@pytest.fixture
def fixture_filtered_deployment_helm_vars_data():
    """
    fixture_filtered_deployment_helm_vars_data
    @return: filtered_deployment_helm_vars_data
    @rtype: dict
    """

    filtered_deployment_helm_vars_data = {
        'my-nginx-deployment': {
            'env': None
        },
        'nginx-deployment': {
            'env': [
                {
                    'name': 'FOO_VARIABLE1',
                    'value': '123'
                },
                {
                    'name': 'FOO_VARIABLE2',
                    'value': '$(FOO_VARIABLE1)'
                },
                {
                    'name': 'FOO_VARIABLE3',
                    'value': 'host_name_example2'
                },
                {
                    'name': 'FOO_VARIABLE4',
                    'value': '$(FOO_VARIABLE3)'
                }
            ],
        }
    }

    return filtered_deployment_helm_vars_data
