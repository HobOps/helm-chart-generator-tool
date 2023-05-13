# -*- coding: utf-8 -*-


class ScriptUtilDictCleaner:
    """
    ScriptUtilDictCleaner
    """

    @classmethod
    def remove_empty_from_dict(cls, d):
        """efficient way to remove keys with empty strings from a dict
        Ref: https://stackoverflow.com/questions/12118695/efficient-way-to-remove-keys-with-empty-strings-from-a-dict"""
        if type(d) is dict:
            return dict((k, cls.remove_empty_from_dict(v)) for k, v in d.items() if v and cls.remove_empty_from_dict(v))
        elif type(d) is list:
            return [cls.remove_empty_from_dict(v) for v in d if v and cls.remove_empty_from_dict(v)]
        else:
            return d

