# -*- coding: utf-8 -*-


# Notes:
"""
The following script its related to v1 original script
Architecture its not defined as its going to be in v2
This is just a wrapper to be able to switch between versions
"""


def str_presenter(dumper, data):
    """configures yaml for dumping multiline strings
    Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data"""
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


class ScriptFileWriterManager:

    @staticmethod
    def write_file(path, values, mode='yaml'):

        import os
        import yaml
        import json

        # Create directory
        directory = os.path.dirname(path)

        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)

        # Write file
        if mode == 'yaml':
            yaml.add_representer(str, str_presenter)
            yaml.representer.SafeRepresenter.add_representer(str, str_presenter)
            with open(path, 'w') as outfile:
                yaml.dump(values, outfile, default_flow_style=False, sort_keys=False)
        elif mode == 'json':
            with open(path, 'w') as outfile:
                json.dump(values, outfile, sort_keys=False, indent=4)
        else:
            with open(path, 'w') as outfile:
                outfile.writelines('\n'.join(values))
        pass


