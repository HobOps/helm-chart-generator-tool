# -*- coding: utf-8 -*-


# Fixtures
from tests.core.modules.config_management.fixtures import fixture_config_settings_data
from tests.core.modules.helm_management.fixtures import fixture_filtered_deployment_helm_vars_data

# Domain
from core.modules.helm_management.helm_vars_management import HelmDeploymentVarsCreator


def test_helm_deployment_vars_data_creator(fixture_config_settings_data, fixture_filtered_deployment_helm_vars_data):
    """
    test_helm_deployment_vars_data_creator
    @param fixture_config_settings_data: fixture_config_settings_data
    @type fixture_config_settings_data: dict
    @param fixture_filtered_deployment_helm_vars_data: fixture_filtered_deployment_helm_vars_data
    @type fixture_filtered_deployment_helm_vars_data: dict
    """

    helm_deployment_vars_creator = HelmDeploymentVarsCreator()
    output_data = helm_deployment_vars_creator.create_vars_data(conf=fixture_config_settings_data)

    assert output_data == fixture_filtered_deployment_helm_vars_data
