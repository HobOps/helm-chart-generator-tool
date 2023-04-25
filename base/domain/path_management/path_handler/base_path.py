# -*- coding: utf-8 -*-


from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BasePath(Protocol):
    """
    BasePath
    """

    def cwd(self):
        """
        cwd
        @return: path
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    def exists(self):
        """
        exists
        @return: exists
        @rtype: bool
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    def joinpath(self, relative_path: str):
        """
        joinpath
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    def mkdir(self, parents: bool = None, exist_ok: bool = None):
        """
        mkdir
        @param parents: parents
        @type parents: bool
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
