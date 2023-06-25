# -*- coding: utf-8 -*-


# Fixtures
from tests.core.modules.config_management.fixtures import fixture_config_settings_data
from tests.core.modules.helm_management.fixtures import fixture_filtered_statefulset_helm_values_config_data

# Domain
from core.modules.helm_management import HelmValuesChartCreator


def test_helm_values_chart_creaator_with_valid_params(
        fixture_config_settings_data,
        fixture_filtered_statefulset_helm_values_config_data,
):
    """
    test_helm_values_chart_creaator_with_valid_params
    @param fixture_config_settings_data: fixture_config_settings_data
    @type fixture_config_settings_data: dict
    @param fixture_filtered_statefulset_helm_values_config_data: fixture_filtered_statefulset_helm_values_config_data
    @type fixture_filtered_statefulset_helm_values_config_data: dict
    """

    env_vars_pattern = r'\$\(.*?\)'

    helm_values_chart_creator = HelmValuesChartCreator(config_data=env_vars_pattern)
    output_data = helm_values_chart_creator.create_values_file(conf=fixture_config_settings_data)

    assert output_data == fixture_filtered_statefulset_helm_values_config_data
