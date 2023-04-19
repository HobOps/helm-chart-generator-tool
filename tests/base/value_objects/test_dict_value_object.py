# -*- coding: utf-8 -*-


import pytest


from base.domain.common.value_objects import DictValueObject


def test_dict_value_object_validation_pass():
    """
    test_dict_value_object_validation_pass
    """

    data = {
        "key1": "value1",
        "key2": "value2"
    }
    data_value = DictValueObject(data)

    assert data_value.value == data


def test_dict_value_object_validation_fails():
    """
    test_dict_value_object_validation_fails
    """

    data = 12345
    expected_error_message = f"Error value: {data} is not a dict type"

    with pytest.raises(ValueError) as err:
        data_value = DictValueObject(data)

    assert err.value.args[0] == expected_error_message


def test_dict_value_object_validation_fails_with_none():
    """
    test_dict_value_object_validation_fails_with_none
    """

    data = None
    expected_error_message = f"Error value: {data} is not a dict type"

    with pytest.raises(ValueError) as err:
        data_value = DictValueObject(data)

    assert err.value.args[0] == expected_error_message



