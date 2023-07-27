# -*- coding: utf-8 -*-


from jinja2 import Template

# Domain
from framework.base.domain.template_management.template_render import BaseTemplateRender


class JinjaTemplateRender(BaseTemplateRender):
    """
    JinjaTemplateRender
    """

    def __init__(self, template_jinja: Template):
        """
        JinjaTemplateRender
        @param template_jinja: template_jinja
        @type template_jinja: BaseTemplateLoader
        """

        if not isinstance(template_jinja, Template):
            raise ValueError(f"Error template_jinja: {template_jinja} is not an instance of {Template}")

        self.__template_jinja = template_jinja

    def render(self, data_to_render: dict):
        """
        render
        @param data_to_render: data_to_render
        @type data_to_render: dict
        @return: content_rendered
        @rtype: str
        """

        if not isinstance(data_to_render, dict):
            raise ValueError(f"Error {data_to_render} is not dict type")

        content_rendered = self.__template_jinja.render(**data_to_render)

        return content_rendered
