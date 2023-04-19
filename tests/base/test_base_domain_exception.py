# -*- coding: utf-8 -*-


import pytest

from base.domain.exceptions import BaseDomainException


def test_base_domain_exception_full_validation():
    """
    test_base_domain_exception_full_validation
    """

    error_message = "My Error Message"
    error_source = "Here starts the source of the error"
    error_type = "Base type"

    my_exception = BaseDomainException(error_message, error_source, error_type)

    with pytest.raises(BaseDomainException):
        raise my_exception

    assert my_exception.args.__len__() == 1
    assert my_exception.error_message == error_message
    assert my_exception.error_source == error_source
    assert my_exception.error_type == error_type


def test_base_domain_exception_minimal_validation():
    """
    test_base_domain_exception_minimal_validation
    """

    error_message = "My Error Message"

    my_exception = BaseDomainException(error_message)

    with pytest.raises(BaseDomainException):
        raise my_exception

    assert my_exception.args.__len__() == 1
    assert my_exception.error_message == error_message
    assert my_exception.error_source is None
    assert my_exception.error_type is None


def test_base_domain_exception_minimal_validation_fails():
    """
    test_base_domain_exception_minimal_validation_fails
    """

    with pytest.raises(Exception):
        my_exception = BaseDomainException()

    assert True

