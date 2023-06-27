# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable

# Domain
from app.app_management.argument_data import ArgumentData


@runtime_checkable
class AppManagerBase(Protocol):
    """
    AppManagerBase
    """

    @staticmethod
    @abstractmethod
    def run(args: ArgumentData):
        """
        run
        @param args: args
        @type args: ArgumentData
        @return: version
        @rtype: int
        """

        raise NotImplementedError(f"{AppManagerBase.__class__.__name__} Interface Missing Implementation")
