# -*- coding: utf-8 -*-


from app.v1.modules.file_manager import ScriptFileWriterManager


class ScriptHelmIgnoreCreator:
    """
    ScriptHelmIgnoreCreator
    """

    @staticmethod
    def create_helmignore_file(conf):
        data = [
            '# Patterns to ignore when building packages.',
            '# This supports shell glob matching, relative path matching, and',
            '# negation (prefixed with !). Only one pattern per line.',
            '.DS_Store',
            '# Common VCS dirs',
            '.git/',
            '.gitignore',
            '.bzr/',
            '.bzrignore',
            '.hg/',
            '.hgignore',
            '.svn/',
            '# Common backup files',
            '*.swp',
            '*.bak',
            '*.tmp',
            '*.orig',
            '*~',
            '# Various IDEs',
            '.project',
            '.idea/',
            '*.tmproj',
            '.vscode/',
            ''
        ]
        ScriptFileWriterManager.write_file(f"config_files/output/charts/{conf['chart']['name']}/.helmignore", data, mode='raw')
        pass
