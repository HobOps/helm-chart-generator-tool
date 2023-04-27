# -*- coding: utf-8 -*-


from base.domain.common.exceptions import BaseDomainException


class FileWriterException(BaseDomainException):
    """
    FileWriterException
    """

    def __init__(self, error_message: str, error_source: str = None, error_type: str = None):
        super().__init__(error_message, error_source, error_type)

    @property
    def error_message(self):
        """
        error_message
        @return: error_message
        @rtype: str
        """

        return super().error_message

    @property
    def error_source(self):
        """
        error_source
        @return: error_source
        @rtype: str
        """

        return super().error_source

    @property
    def error_type(self):
        """
        error_type
        @return: error_type
        @rtype: str
        """

        return super().error_type

