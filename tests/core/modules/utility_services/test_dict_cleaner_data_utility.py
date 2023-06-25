# -*- coding: utf-8 -*-


# Fixtures
from tests.core.modules.config_management.fixtures import fixture_config_settings_data

# Domain
from core.modules.utility_services import DictCleanerDataUtility


def test_dict_cleaner_data_utility(fixture_config_settings_data):
    """
    test_dict_cleaner_data_utility
    @param fixture_config_settings_data: fixture_config_settings_data
    @type fixture_config_settings_data: dict
    """

    remove_empty_from_dict = DictCleanerDataUtility()
    config_settings_data_cleaned = remove_empty_from_dict.process(fixture_config_settings_data)

    assert config_settings_data_cleaned
