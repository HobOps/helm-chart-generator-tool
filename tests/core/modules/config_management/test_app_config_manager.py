# -*- coding: utf-8 -*-


import pytest


# Infrastructure
from framework.base.infrastructure.file_management.file_doubles import FileFaker
from framework.base.infrastructure.file_management.file_handler import FileHandler
from framework.base.infrastructure.path_management.path_doubles import PathFaker

# Application
from core.modules.config_management import AppConfigManager

# Domain
from framework.base.domain.file_management.file_constants.file_mode_values import file_mode_values
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.path_management.path_constants.path_type_values import path_types_values


def test_app_config_manager_with_valid_params():
    """
    test_app_config_manager_with_valid_params
    """

    file_name = "config_file"
    root_path = '/home/user1'
    path_folder = '/project1/folder1'
    path_file = f'/{file_name}.ini'
    target_path_folder = root_path + path_folder
    target_path_file = root_path + path_folder + path_file

    initial_content = """
       [components]
       ComponentType1:
           component-html
       componentType2:
           component-nginx
       component-type3:
           component-ingress
       componentTypEs4:
           component-serViceS1
           component-serViceS2
           component-serViceS3
       """

    config_data = {
        'components': {
            'ComponentType1': '\ncomponent-HTML',
            'componentType2': '\ncomponent-NginX',
            'component-type3': '\ncomponent-inGress',
            'componentTypEs4': '\ncomponent-serViceS1,    \ncomponent-serViceS2,    \ncomponent-serViceS3,'
        },
    }

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_values.ini, initial_content=initial_content)
    fake_file.open()

    fake_folder_path = PathFaker(target_path=target_path_folder, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(
        target_path=target_path_file,
        target_path_type=path_types_values.file,
        parent_path=fake_folder_path,
        file_obj=fake_file,
    )
    fake_file_path.touch()

    file_handler = FileHandler(path_obj=fake_file_path, file_obj=fake_file, file_mode=file_mode_values.read)

    config_manager = AppConfigManager(root_path=root_path, path_obj=fake_file_path, file_handler=file_handler, config_data=config_data)
    config_data_result = config_manager.parse_config(component_name=file_name)

    assert config_data_result['components']['ComponentType1'] == ['component-HTML']
    assert config_data_result['components']['componentType2'] == ['component-NginX']
    assert config_data_result['components']['component-type3'] == ['component-inGress']
    assert config_data_result['components']['componentTypEs4'] == ['component-serViceS1', 'component-serViceS2', 'component-serViceS3']


def test_app_config_manager_with_not_valid_params():
    """
    test_app_config_manager_with_not_valid_params
    """

    file_name = "config_file"
    root_path = '/home/user1'
    path_folder = '/project1/folder1'
    path_file = f'/{file_name}.ini'
    target_path_folder = root_path + path_folder
    target_path_file = root_path + path_folder + path_file

    initial_content = """
       [components]
       ComponentType1:
           component-html
       componentType2:
           component-nginx
       component-type3:
           component-ingress
       componentTypEs4:
           component-serViceS1
           component-serViceS2
           component-serViceS3
       """

    config_data = ['component1', 'component2']

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_values.ini, initial_content=initial_content)

    fake_folder_path = PathFaker(target_path=target_path_folder, target_path_type=path_types_values.directory)
    fake_file_path = PathFaker(
        target_path=target_path_file,
        target_path_type=path_types_values.file,
        parent_path=fake_folder_path,
        file_obj=fake_file,
    )

    file_handler = FileHandler(path_obj=fake_file_path, file_obj=fake_file, file_mode=file_mode_values.read)

    expected_error_message = f"Error config_data: {config_data} is not dict type"

    with pytest.raises(ValueError) as err:
        config_manager = AppConfigManager(root_path=root_path, path_obj=fake_folder_path, file_handler=file_handler, config_data=config_data)

    assert err.value.args[0] == expected_error_message

