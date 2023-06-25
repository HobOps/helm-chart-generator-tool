# -*- coding: utf-8 -*-


from core.modules.helm_management .helm_values_chart_management import HelmValuesDataProcessing
from tests.core.modules.helm_management.dummies.dummy_values_extract_data_filter import DummyValuesExtractDataFilter
from tests.core.modules.helm_management.dummies.dummy_values_remove_data_filter import DummyValuesRemoveDataFilter


def test_helm_values_data_processing_with_valid_dummies():
    """
    test_helm_values_data_processing_with_valid_dummies
    """

    input_data = {
        "valid_key": {
            "valid_key1": "value1",
            "valid_key2": "value2",
            "valid_key3": "value3",
            "not_good_key": {
                "not_good_key1": "value1",
                "not_good_key2": "value2",
                "not_good_key3": "value3",
            },
        },
        "dummy_key": {
            "dummy1": "value1",
            "dummy2": "value2",
            "dummy3": "value3",
        },
    }

    expected_filtered_data = {
        "valid_key1": "value1",
        "valid_key2": "value2",
        "valid_key3": "value3",
    }

    config_data1 = "valid_key"
    config_data2 = "not_good_key"

    first_filter = DummyValuesExtractDataFilter(config_data=config_data1)
    second_filter = DummyValuesRemoveDataFilter(config_data=config_data2)

    helm_pipeline = HelmValuesDataProcessing().add_handler(first_filter).add_handler(second_filter)
    output_data = helm_pipeline.execute(input_data=input_data)

    assert output_data == expected_filtered_data
