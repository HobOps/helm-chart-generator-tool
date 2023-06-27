# -*- coding: utf-8 -*-


from settings import Settings


# Infrastructure
from framework.base.infrastructure.config_management.config_mapper import ConfigMapper
from framework.base.infrastructure.config_management.config_reader import ConfigReader
from framework.base.infrastructure.file_management.file_doubles import FileFaker
from framework.base.infrastructure.file_management.file_handler import FileHandler
from framework.base.infrastructure.path_management.path_doubles import PathFaker
from framework.base.infrastructure.path_management.path_factory import SimplePathCreator

# Domain
from framework.base.domain.file_management.file_constants.file_mode_values import file_mode_values
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.path_management.path_constants import path_types_values


def test_config_reader_with_current_params():
    """
    test_config_reader_with_current_params
    """

    filter_sections = ['DEFAULT']

    root_path = Settings.get_root_path().as_posix()
    target_path = '/config_files/input/configurations/k3s01-nginx-test.ini'

    path_creator = SimplePathCreator(root_path=root_path)
    created_path = path_creator.generate_path(target_path=target_path)

    config_reader = ConfigReader(path_obj=created_path)
    config_parser = config_reader.get_config_parser()

    config_mapper = ConfigMapper(
        config_parser=config_parser,
        filter_sections=filter_sections,
    )
    config_data = config_mapper.map_config_data()

    assert config_data['components']['ConfigMap'] == ['example-html']
    assert config_data['components']['Deployment'] == ['nginx-deployment', 'my-nginx-deployment']
    assert config_data['components']['Ingress'] == ['nginx-deployment']


def test_config_reader_with_valid_params():
    """
    test_config_reader_with_valid_params
    """

    filter_sections = ['DEFAULT']

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

    file_handler = FileHandler(file_mode=file_mode_values.read, path_obj=fake_file_path, file_obj=fake_file)

    config_reader = ConfigReader(path_obj=fake_file_path, file_handler=file_handler, config_data=config_data)
    config_parser = config_reader.get_config_parser()

    config_mapper = ConfigMapper(
        config_parser=config_parser,
        filter_sections=filter_sections,
    )
    config_data = config_mapper.map_config_data()

    assert config_data['components']['ComponentType1'] == ['component-HTML']
    assert config_data['components']['componentType2'] == ['component-NginX']
    assert config_data['components']['component-type3'] == ['component-inGress']
    assert config_data['components']['componentTypEs4'] == ['component-serViceS1', 'component-serViceS2', 'component-serViceS3']
