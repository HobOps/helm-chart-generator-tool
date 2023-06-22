# -*- coding: utf-8 -*-


import argparse

# Infrastructure
from framework.base.infrastructure.cli_management.argument_parser import ArgumentParser


def test_argument_parser_with_valid_params():
    """
    test_argument_parser_with_valid_params
    """

    arguments_input = {
        "name": "Dummy Name for CLI Tests",
        "version": "Dummy Version for CLI Tests",
    }

    arguments_output = {
        "name": "dummy_name",
        "version": "dummy_version",
    }

    argument_parser_spy = argparse.ArgumentParser(description="Test")

    argument_parser = ArgumentParser(argument_parser=argument_parser_spy, args=arguments_output)
    argument_parser.add_arguments(args_config=arguments_input)
    args = argument_parser.parse_arguments()

    assert argument_parser.args_config == arguments_input
    assert args == arguments_output
