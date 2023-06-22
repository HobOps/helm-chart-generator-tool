# -*- coding: utf-8 -*-


from core.modules.helm_management import HelmValuesDataProcessing
from core.modules.helm_management import HelmValuesExtractDataFilter
from core.modules.helm_management import HelmValuesRemoveDataFilter


def test_helm_values_data_processing_with_valid_params():
    """
    test_helm_values_data_processing_with_valid_params
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

    first_filter = HelmValuesExtractDataFilter(config_data=config_data1)
    second_filter = HelmValuesRemoveDataFilter(config_data=config_data2)

    helm_pipeline = HelmValuesDataProcessing().add_handler(first_filter).add_handler(second_filter)
    output_data = helm_pipeline.execute(input_data=input_data)

    assert output_data == expected_filtered_data
