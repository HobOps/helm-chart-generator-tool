# -*- coding: utf-8 -*-


import pytest


from base.domain.value_objects import ListValueObject


def test_list_value_object_validation_pass():
    """
    test_list_value_object_validation_pass
    """

    data = ["data1", "data2"]
    data_value = ListValueObject(data)

    assert data_value.value == data


def test_list_value_object_validation_fails():
    """
    test_list_value_object_validation_fails
    """

    data = 12345
    expected_error_message = f"Error value: {data} is not a list type"

    with pytest.raises(ValueError) as err:
        data_value = ListValueObject(data)

    assert err.value.args[0] == expected_error_message


def test_list_value_object_validation_fails_with_none():
    """
    test_list_value_object_validation_fails_with_none
    """

    data = None
    expected_error_message = f"Error value: {data} is not a list type"

    with pytest.raises(ValueError) as err:
        data_value = ListValueObject(data)

    assert err.value.args[0] == expected_error_message



