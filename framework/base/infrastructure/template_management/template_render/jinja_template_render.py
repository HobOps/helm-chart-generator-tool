# -*- coding: utf-8 -*-


# Domain
from framework.base.domain.path_management.path_doubles import BasePath
from framework.base.domain.template_management.template_loader import BaseTemplateLoader
from framework.base.domain.template_management.template_render import BaseTemplateRender


class JinjaTemplateRender(BaseTemplateRender):
    """
    JinjaTemplateRender
    """

    def __init__(self, template_loader: BaseTemplateLoader = None):
        """
        JinjaTemplateRender
        @param template_loader: template_loader
        @type template_loader: BaseTemplateLoader
        """

        if not isinstance(template_loader, (BaseTemplateLoader, type(None))):
            raise ValueError(f"Error template_loader: {template_loader} is not an instance of {BaseTemplateLoader}")

        self.__template_loader = template_loader

    def render(self, template_path: BasePath, content: str):
        """
        render
        @param template_path: template_path
        @type template_path: BasePath
        @param content: content
        @type content: str
        @return: template_render
        @rtype: str
        """

        if not isinstance(template_path, BasePath):
            raise ValueError(f"Error {template_path} is not an instance of {BasePath}")

        if not isinstance(content, str):
            raise ValueError(f"Error {content} is not str type")

        template = self.__template_loader.get_template(template_path.as_posix())
        template_render = template.render(content)

        return template_render