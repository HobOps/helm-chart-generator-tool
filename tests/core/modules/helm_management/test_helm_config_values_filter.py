# -*- coding: utf-8 -*-


# Fixtures
from tests.core.modules.config_management.fixtures import fixture_config_settings_clean_data
from tests.core.modules.helm_management.fixture import fixture_filtered_helm_values_config_data

# Domain
from core.modules.helm_management import HelmConfigValuesFilter


def test_helm_config_values_filter(fixture_config_settings_clean_data, fixture_filtered_helm_values_config_data):
    """
    test_helm_config_values_filter
    @param fixture_config_settings_clean_data: fixture_config_settings_clean_data
    @type fixture_config_settings_clean_data: dict
    @param fixture_filtered_helm_values_config_data: fixture_filtered_helm_values_config_data
    @type fixture_filtered_helm_values_config_data: dict
    """

    helm_config_values_filter = HelmConfigValuesFilter()
    helm_values_data_filtered = helm_config_values_filter.process(conf=fixture_config_settings_clean_data)

    assert helm_values_data_filtered == fixture_filtered_helm_values_config_data
    