# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable

# Domain
from framework.base.domain.path_management.path_doubles import BasePath


@runtime_checkable
class BaseTemplateLoader(Protocol):
    """
    BaseTemplateLoader
    """

    @abstractmethod
    def get_template(self, path_obj: BasePath):
        """
        get_template
        @param path_obj: path_obj
        @type path_obj: BasePath
        @return: template
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
