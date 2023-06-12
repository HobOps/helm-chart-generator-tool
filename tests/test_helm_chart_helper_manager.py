# -*- coding: utf-8 -*-


import argparse
from unittest.mock import Mock

# Infrastructure
from base.infrastructure.cli_management.argument_parser import ArgumentParser

# Application
from helm_chart_helper_manager import HelmChartHelperManager
from app.app_management import AppVersionCreator
from app.v1.script import AppMainManagerV10
from app.v2.main import AppMainManagerV21
from app.v2.main import AppMainManagerV22


def test_helm_chart_helper_manager_with_valid_params_v10():
    """
    test_helm_chart_helper_manager_with_valid_params_v10
    """

    app_version_factory = AppVersionCreator()
    app_manager = AppMainManagerV10()
    expected_app_version = "10"

    argument_input = {
        "name": "dummy_name_test",
        "version": expected_app_version,
    }

    args_parser = ArgumentParser(args=argument_input)

    # Mocks
    app_manager.run = Mock(return_value=expected_app_version)
    app_version_factory.create_app = Mock(return_value=app_manager)

    helm_chart_helper_manager = HelmChartHelperManager(args_parser=args_parser, app_version_factory=app_version_factory)
    app_version = helm_chart_helper_manager.run()

    assert app_version == expected_app_version
    assert app_version_factory.create_app.call_count >= 1


def test_helm_chart_helper_manager_with_valid_params_v21():
    """
    test_helm_chart_helper_manager_with_valid_params_v21
    """

    app_version_factory = AppVersionCreator()
    app_manager = AppMainManagerV21()
    expected_app_version = "21"

    argument_input = {
        "name": "dummy_name_test",
        "version": expected_app_version,
    }

    args_parser = ArgumentParser(args=argument_input)

    # Mocks
    app_manager.run = Mock(return_value=expected_app_version)
    app_version_factory.create_app = Mock(return_value=app_manager)

    helm_chart_helper_manager = HelmChartHelperManager(args_parser=args_parser, app_version_factory=app_version_factory)
    app_version = helm_chart_helper_manager.run()

    assert app_version == expected_app_version
    assert app_version_factory.create_app.call_count >= 1


def test_helm_chart_helper_manager_with_valid_params_v22():
    """
    test_helm_chart_helper_manager_with_valid_params_v22
    """

    app_version_factory = AppVersionCreator()
    app_manager = AppMainManagerV22()
    expected_app_version = "22"

    argument_input = {
        "name": "dummy_name_test",
        "version": expected_app_version,
    }

    args_parser = ArgumentParser(args=argument_input)

    # Mocks
    app_manager.run = Mock(return_value=expected_app_version)
    app_version_factory.create_app = Mock(return_value=app_manager)

    helm_chart_helper_manager = HelmChartHelperManager(args_parser=args_parser, app_version_factory=app_version_factory)
    app_version = helm_chart_helper_manager.run()

    assert app_version == expected_app_version
    assert app_version_factory.create_app.call_count >= 1


