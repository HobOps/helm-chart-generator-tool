# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable

# Application
from app.app_management import AppManagerBase


@runtime_checkable
class AppVersionCreatorBase(Protocol):
    """
    AppVersionCreatorBase
    """

    @abstractmethod
    def create_app(self, version: str):
        """
        run
        @param version: version
        @type version: str
        @return: app_manager
        @rtype: AppManagerBase
        """

        raise NotImplementedError(f"{AppVersionCreatorBase.__class__.__name__} Interface Missing Implementation")
