# -*- coding: utf-8 -*-


from jinja2 import Environment
from jinja2 import FileSystemLoader

# Domain
from framework.base.domain.path_management.path_doubles import BasePath
from framework.base.domain.template_management.template_loader import BaseTemplateLoader


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
        self.__loader = FileSystemLoader(self.__template_dir_path.as_posix())
        self.__environment = Environment(loader=self.__loader)

    def get_template(self, path_obj: BasePath):
        """
        get_template
        @param path_obj: path_obj
        @type path_obj: BasePath
        @return: template
        @rtype: str
        """

        template = self.__environment.get_template(path_obj.as_posix())

        return template
