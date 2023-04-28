# -*- coding: utf-8 -*-


from pathlib import Path


# Domain
from base.domain.path_management.path_doubles import BasePath


class PathItem(BasePath):
    """
    PathItem
    """

    def __init__(self, target_path: str):
        """
        PathItem
        """

        self.__target_path = target_path
        self.__stored_path = Path(target_path)

    def as_posix(self):
        """
        as_posix
        @return: as_posix
        @rtype: str
        """

        return self.__stored_path.as_posix()

    def exists(self):
        """
        exists
        @return: exists
        @rtype: bool
        """

        return self.__stored_path.exists()
    
    def is_dir(self):
        """
        is_dir
        @return: is_dir
        @rtype: bool
        """

        return self.__stored_path.is_dir()

    def is_file(self):
        """
        is_file
        @return: is_file
        @rtype: bool
        """

        return self.__stored_path.is_file()

    def joinpath(self, relative_path: str):
        """
        joinpath
        @return: None
        @rtype: None
        """

        return self.__stored_path.joinpath(relative_path)

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

        return self.__stored_path.mkdir()

    @property
    def parent(self):
        """
        parent
        @return: parent
        @rtype: str
        """

        return self.__stored_path.parent

    @property
    def suffix(self):
        """
        suffix
        @return: None
        @rtype: None
        """

        return self.__stored_path.suffix
    
    def touch(self, exist_ok: bool = None):
        """
        touch
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        return self.__stored_path.touch()

