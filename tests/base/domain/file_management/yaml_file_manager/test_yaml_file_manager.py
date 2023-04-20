# -*- coding: utf-8 -*-


import yaml
from unittest.mock import MagicMock
from unittest.mock import Mock


def test_yaml_file_management_validation():
    """
    test_yaml_file_management_validation
    """

    yaml_info = """
    # Example
    cluster:
      context: default
      namespace: default
      version: 1.0
    """
    my_data1 = yaml.unsafe_load(yaml_info)
    my_data2 = yaml.safe_load(yaml_info)

    dumped_data = Mock()
    yaml.dump(yaml_info, dumped_data)

    assert my_data1["cluster"]["context"] == "default"
    assert my_data2["cluster"]["context"] == "default"

    assert dumped_data.mock_calls[0][0] == 'write'
    assert dumped_data.write.mock_calls.__len__() > 0
    assert True
