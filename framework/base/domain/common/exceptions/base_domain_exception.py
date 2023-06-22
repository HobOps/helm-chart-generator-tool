# -*- coding: utf-8 -*-


class BaseDomainException(Exception):
    """
    BaseDomainException
    """

    def __init__(self, error_message: str, error_source: str = None, error_type: str = None):
        """
        BaseDomainException
        @param error_message: error_message
        @type error_message: str
        @param error_source: error_source
        @type error_source: str
        @param error_type: error_type
        @type error_type: str
        """

        if not isinstance(error_message, str):
            raise ValueError(f"Error error_message: {error_message} is not str type")

        if not isinstance(error_source, (str, type(None))):
            raise ValueError(f"Error error_source: {error_source} is not str type")

        if not isinstance(error_type, (str, type(None))):
            raise ValueError(f"Error error_type: {error_type} is not str type")

        super().__init__(error_message)

        self.__error_message = error_message
        self.__error_source = error_source
        self.__error_type = error_type

    @property
    def error_message(self):
        """
        error_message
        @return: error_message
        @rtype: str
        """

        return self.__error_message

    @property
    def error_source(self):
        """
        error_source
        @return: error_source
        @rtype: str
        """

        return self.__error_source

    @property
    def error_type(self):
        """
        error_type
        @return: error_type
        @rtype: str
        """

        return self.__error_type



