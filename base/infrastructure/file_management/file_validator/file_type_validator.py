# -*- coding: utf-8 -*-


# Domain
from base.domain.file_management.file_constants import file_type_values
from base.domain.file_management.file_validator import BaseFileTypeValidator


class FileTypeValidator(BaseFileTypeValidator):
    """
    FileTypeValidator
    """

    @staticmethod
    def validate_file_type(file_type: str):
        """
        validate_file_type
        @param file_type: file_type
        @type file_type: str
        @return: is_valid
        @rtype: bool
        """

        if not isinstance(file_type, str):
            raise ValueError(f"Error file_type: {file_type} is not str type")

        if file_type in file_type_values.__match_args__:
            return True

        return False

    @staticmethod
    def validate_file_type_suffix(file_type_suffix: str):
        """
        validate_file_type_suffix
        @param file_type_suffix: file_type_suffix
        @type file_type_suffix: str
        @return: is_valid
        @rtype: bool
        """

        if not isinstance(file_type_suffix, str):
            raise ValueError(f"Error file_type_suffix: {file_type_suffix} is not str type")

        valid_file_types = [value for key, value in file_type_values.__dict__.items()]

        if file_type_suffix in valid_file_types:
            return True

        return False

