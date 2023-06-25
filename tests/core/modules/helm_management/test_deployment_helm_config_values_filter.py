# -*- coding: utf-8 -*-


# Fixtures
from tests.core.modules.helm_management.fixture import fixture_filtered_deployment_helm_values_config_data
from tests.core.modules.helm_management.fixture import fixture_filtered_helm_values_config_data

# Domain
from core.modules.helm_management import HelmDeployEnvVarsFilter


def test_deployment_helm_config_values_filter(fixture_filtered_helm_values_config_data, fixture_filtered_deployment_helm_values_config_data):
    """
    test_deployment_helm_config_values_filter
    @param fixture_filtered_helm_values_config_data: fixture_filtered_helm_values_config_data
    @type fixture_filtered_helm_values_config_data: dict
    @param fixture_filtered_deployment_helm_values_config_data: fixture_filtered_deployment_helm_values_config_data
    @type fixture_filtered_deployment_helm_values_config_data: dict
    """

    env_var_pattern = r'\$\(.*?\)'

    helm_deployment_env_vars_filter = HelmDeployEnvVarsFilter(config_data=env_var_pattern)
    helm_values_data_filtered = helm_deployment_env_vars_filter.process(conf=fixture_filtered_helm_values_config_data)

    assert helm_values_data_filtered == fixture_filtered_deployment_helm_values_config_data
