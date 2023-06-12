# -*- coding: utf-8 -*-


# Infrastructure
import argparse

# Domain
from base.domain.cli_management.argument_parser import BaseArgumentParser


class ArgumentParser(BaseArgumentParser):
    """
    ArgumentParser
    """

    def __init__(self, argument_parser: argparse.ArgumentParser = None, args: dict = None):
        """
        ArgumentParser
        @param argument_parser: argument_parser
        @type argument_parser: argparse.ArgumentParser
        @param args: args
        @type args: dict
        """

        if not isinstance(argument_parser, (argparse.ArgumentParser, type(None))):
            raise ValueError(f"Error argument_parser: {argument_parser} is not an instance of {argparse.ArgumentParser}")

        if not isinstance(args, (dict, type(None))):
            raise ValueError(f"Error args: {args} is not dict type")

        self.__argument_parser = argument_parser or argparse.ArgumentParser(description='CLI Argument Parser')
        self.__args_config = None
        self.__args = args

    def add_arguments(self, args_config: dict):
        """
        add_arguments
        @param args_config: args_config
        @type args_config: dict
        @return: None
        @rtype: None
        """

        if not isinstance(args_config, dict):
            raise ValueError(f"Error args: {args_config} is not list type")

        for argument, description in args_config.items():
            self.__argument_parser.add_argument(f'--{argument}', action='store', type=str, help=f"{description}")

        self.__args_config = args_config

    def parse_arguments(self):
        """
        parse_arguments
        @return: args
        @rtype: dict
        """

        args = self.__args or self.__argument_parser.parse_args().__dict__

        return args

    @property
    def args_config(self):
        """
        args_config
        @return: args_config
        @rtype: dict
        """

        return self.__args_config

