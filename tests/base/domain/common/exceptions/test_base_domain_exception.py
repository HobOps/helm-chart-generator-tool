# -*- coding: utf-8 -*-


import pytest

from base.domain.common.exceptions import BaseDomainException


def test_base_domain_exception_full_validation():
    """
    test_base_domain_exception_full_validation
    """

    error_message = "My Error Message"
    error_source = "Here starts the source of the error"
    error_type = "Base type"

    my_exception = BaseDomainException(error_message, error_source, error_type)

    with pytest.raises(BaseDomainException) as err:
        raise my_exception

    assert my_exception.args.__len__() == 1
    assert my_exception.error_message == err.value.error_message
    assert my_exception.error_source == err.value.error_source
    assert my_exception.error_type == err.value.error_type


def test_base_domain_exception_minimal_validation():
    """
    test_base_domain_exception_minimal_validation
    """

    error_message = "My Error Message"

    my_exception = BaseDomainException(error_message)

    with pytest.raises(BaseDomainException) as err:
        raise my_exception

    assert my_exception.args.__len__() == 1
    assert my_exception.error_message == err.value.error_message
    assert my_exception.error_source is None
    assert my_exception.error_type is None


def test_base_domain_exception_minimal_validation_fails():
    """
    test_base_domain_exception_minimal_validation_fails
    """

    expected_error_message = "__init__() missing 1 required positional argument: 'error_message'"

    with pytest.raises(Exception) as err:
        my_exception = BaseDomainException()

    assert err.value.args[0] == expected_error_message

