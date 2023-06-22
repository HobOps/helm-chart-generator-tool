# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BasePath(Protocol):
    """
    BasePath
    """

    @abstractmethod
    def as_posix(self):
        """
        as_posix
        @return: as_posix
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def exists(self):
        """
        exists
        @return: exists
        @rtype: bool
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def is_dir(self):
        """
        is_dir
        @return: is_dir
        @rtype: bool
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def is_file(self):
        """
        is_file
        @return: is_file
        @rtype: bool
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
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

    @property
    @abstractmethod
    def parent(self):
        """
        parent
        @return: parent
        @rtype: str
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @property
    @abstractmethod
    def suffix(self):
        """
        suffix
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def touch(self, exist_ok: bool = None):
        """
        touch
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

