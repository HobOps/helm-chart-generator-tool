# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable

# Domain
from framework.base.domain.template_management.template_render import BaseTemplateRender


@runtime_checkable
class BaseTemplateLoader(Protocol):
    """
    BaseTemplateLoader
    """

    @abstractmethod
    def get_template(self, template_name: str) -> BaseTemplateRender:
        """
        get_template
        @param template_name: template_name
        @type template_name: str
        @return: template
        @rtype: BaseTemplateRender
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
