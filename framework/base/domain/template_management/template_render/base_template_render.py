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
    def render(self, data_to_render: dict):
        """
        render
        @param data_to_render: data_to_render
        @type data_to_render: dict
        @return: content_rendered
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
