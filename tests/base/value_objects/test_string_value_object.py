# -*- coding: utf-8 -*-


import pytest


from base.domain.common.value_objects import StringValueObject


def test_string_value_object_validation_pass():
    """
    test_string_value_object_validation_pass
    """

    text = "My Text Value to Test"
    text_value = StringValueObject(text)

    assert text_value.value == text


def test_string_value_object_validation_fails():
    """
    test_string_value_object_validation_fails
    """

    text = 12345
    expected_error_message = f"Error value: {text} is not a str type"

    with pytest.raises(ValueError) as err:
        text_value = StringValueObject(text)

    assert err.value.args[0] == expected_error_message


def test_string_value_object_validation_fails_with_none():
    """
    test_string_value_object_validation_fails
    """

    text = None
    expected_error_message = f"Error value: {text} is not a str type"

    with pytest.raises(ValueError) as err:
        text_value = StringValueObject(text)

    assert err.value.args[0] == expected_error_message



