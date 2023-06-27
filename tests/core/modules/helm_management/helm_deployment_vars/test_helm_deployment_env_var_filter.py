# -*- coding: utf-8 -*-


# Fixtures
from tests.core.modules.helm_management.fixtures import fixture_filtered_common_library_config_data
from tests.core.modules.helm_management.fixtures import fixture_filtered_deployment_helm_vars_data

# Domain
from core.modules.helm_management.helm_deployment_vars import HelmDeploymentEnvVarsFilter


def test_helm_deployment_env_vars_filter_with_valid_params(
        fixture_filtered_common_library_config_data,
        fixture_filtered_deployment_helm_vars_data,
):
    """
    test_helm_deployment_env_vars_filter_with_valid_params
    @param fixture_filtered_helm_values_config_data: fixture_filtered_helm_values_config_data
    @type fixture_filtered_helm_values_config_data: dict
    @param fixture_filtered_deployment_helm_vars_data: fixture_filtered_deployment_helm_vars_data
    @type fixture_filtered_deployment_helm_vars_data: dict
    """

    helm_deployment_env_vars_filter = HelmDeploymentEnvVarsFilter()
    output_data = helm_deployment_env_vars_filter.process(fixture_filtered_common_library_config_data)

    assert output_data == fixture_filtered_deployment_helm_vars_data

