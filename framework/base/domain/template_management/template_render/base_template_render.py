# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable

# Domain
from framework.base.domain.path_management.path_doubles import BasePath


@runtime_checkable
class BaseTemplateRender(Protocol):
    """
    BaseTemplateRender
    """

    @abstractmethod
    def render(self, template_path: BasePath, content: str):
        """
        render
        @param template_path: template_path
        @type template_path: BasePath
        @param content: content
        @type content: str
        @return: template_rendered
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
