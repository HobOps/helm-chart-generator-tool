# -*- coding: utf-8 -*-


# Application
from app.app_management import AppVersionCreatorBase
from app.app_management import AppManagerBase
from app.v1.script import AppMainManagerV10
from app.v2.main import AppMainManagerV21
from app.v2.main import AppMainManagerV22


class AppVersionCreator(AppVersionCreatorBase):
    """
    AppVersionCreator
    """

    def create_app(self, app_version: str):
        """
        create_app
        @param app_version: app_version
        @type app_version: str
        @return: AppManager
        @rtype: AppManagerBase
        """

        if not isinstance(app_version, str):
            raise ValueError(f"Error app_version: {app_version} is not str type")

        app_manager = getattr(self, f"app_version_{app_version}")

        return app_manager()

    @staticmethod
    def app_version_10():
        """
        app_version_10
        @return: AppMainManagerV10
        @rtype: AppManagerBase
        """

        return AppMainManagerV10()

    @staticmethod
    def app_version_21():
        """
        app_version_21
        @return: AppMainManagerV21
        @rtype: AppManagerBase
        """

        return AppMainManagerV21()

    @staticmethod
    def app_version_22():
        """
        app_version_22
        @return: AppMainManagerV22
        @rtype: AppManagerBase
        """

        return AppMainManagerV22()

