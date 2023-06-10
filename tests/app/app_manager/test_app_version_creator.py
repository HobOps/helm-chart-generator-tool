# -*- coding: utf-8 -*-


from app.app_management import AppVersionCreator
from app.app_management import AppManagerBase
from app.v1.script import AppMainManagerV10
from app.v2.main import AppMainManagerV21
from app.v2.main import AppMainManagerV22


def test_app_version_creator_with_valid_params_v10():
    """
    test_app_version_creator_with_valid_params_v10
    """

    app_version_factory = AppVersionCreator()
    app = app_version_factory.create_app("10")

    assert type(app) == AppMainManagerV10
    assert isinstance(app, AppManagerBase)


def test_app_version_creator_with_valid_params_v21():
    """
    test_app_version_creator_with_valid_params_v21
    """

    app_version_factory = AppVersionCreator()
    app = app_version_factory.create_app("21")

    assert type(app) == AppMainManagerV21
    assert isinstance(app, AppManagerBase)


def test_app_version_creator_with_valid_params_v22():
    """
    test_app_version_creator_with_valid_params_v22
    """

    app_version_factory = AppVersionCreator()
    app = app_version_factory.create_app("22")

    assert type(app) == AppMainManagerV22
    assert isinstance(app, AppManagerBase)

