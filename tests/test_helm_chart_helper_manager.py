# -*- coding: utf-8 -*-


import argparse
from unittest.mock import Mock


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

    args_parser = argparse.ArgumentParser(description="Stub for Testings")
    app_version_factory = AppVersionCreator()
    app_manager = AppMainManagerV10()
    expected_app_version = "10"

    # Mocks
    args_parser.parse_args = Mock(return_value=None)
    app_manager.run = Mock(return_value=expected_app_version)
    app_version_factory.create_app = Mock(return_value=app_manager)

    helm_chart_helper_manager = HelmChartHelperManager(args_parser=args_parser, app_version_factory=app_version_factory)
    app_version = helm_chart_helper_manager.run(name="config_dummy_file", version=expected_app_version)

    assert app_version == expected_app_version
    assert args_parser.parse_args.call_count >= 1
    assert app_version_factory.create_app.call_count >= 1


def test_helm_chart_helper_manager_with_valid_params_v21():
    """
    test_helm_chart_helper_manager_with_valid_params_v21
    """

    args_parser = argparse.ArgumentParser(description="Stub for Testings")
    app_version_factory = AppVersionCreator()
    app_manager = AppMainManagerV21()
    expected_app_version = "21"

    # Mocks
    args_parser.parse_args = Mock(return_value=None)
    app_manager.run = Mock(return_value=expected_app_version)
    app_version_factory.create_app = Mock(return_value=app_manager)

    helm_chart_helper_manager = HelmChartHelperManager(args_parser=args_parser, app_version_factory=app_version_factory)
    app_version = helm_chart_helper_manager.run(name="config_dummy_file", version=expected_app_version)

    assert app_version == expected_app_version
    assert args_parser.parse_args.call_count >= 1
    assert app_version_factory.create_app.call_count >= 1


def test_helm_chart_helper_manager_with_valid_params_v22():
    """
    test_helm_chart_helper_manager_with_valid_params_v22
    """

    args_parser = argparse.ArgumentParser(description="Stub for Testings")
    app_version_factory = AppVersionCreator()
    app_manager = AppMainManagerV22()
    expected_app_version = "22"

    # Mocks
    args_parser.parse_args = Mock(return_value=None)
    app_manager.run = Mock(return_value=expected_app_version)
    app_version_factory.create_app = Mock(return_value=app_manager)

    helm_chart_helper_manager = HelmChartHelperManager(args_parser=args_parser, app_version_factory=app_version_factory)
    app_version = helm_chart_helper_manager.run(name="config_dummy_file", version=expected_app_version)

    assert app_version == expected_app_version
    assert args_parser.parse_args.call_count >= 1
    assert app_version_factory.create_app.call_count >= 1


