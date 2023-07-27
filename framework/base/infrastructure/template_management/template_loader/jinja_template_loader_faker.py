# -*- coding: utf-8 -*-


from jinja2 import Environment
from jinja2 import FileSystemLoader

# Infrastructure
from framework.base.infrastructure.template_management.template_render import JinjaTemplateRender

# Domain
from framework.base.domain.path_management.path_doubles import BasePath
from framework.base.domain.template_management.template_loader import BaseTemplateLoader
from framework.base.domain.template_management.template_render import BaseTemplateRender


class JinjaTemplateLoader(BaseTemplateLoader):
    """
    JinjaTemplateLoader
    """

    def __init__(self, template_dir_path: BasePath):
        """
        JinjaTemplateLoader
        @param template_dir_path: template_dir_path
        @type template_dir_path: BasePath
        """

        if not isinstance(template_dir_path, BasePath):
            raise ValueError(f"Error template_dir_path: {template_dir_path} is not an instance of {BasePath}")

        self.__template_dir_path = template_dir_path
        self.__environment = Environment()

    def get_template(self, template_name: str):
        """
        get_template
        @param template_name: template_name
        @type template_name: str
        @return: template_jinja
        @rtype: BaseTemplateRender
        """

        if not isinstance(template_name, str):
            raise ValueError(f"Error template_name")

        template = self.__environment.from_string("dummy_str")
        template_jinja = JinjaTemplateRender(template_jinja=template)

        return template_jinja

    @property
    def environment(self):
        """
        environment
        @return: environment
        @rtype: Environment
        """

        return self.__environment

    @property
    def template_dir_path(self):
        """
        template_dir_path
        @return: template_dir_path
        @rtype: BasePath
        """

        return self.__template_dir_path
