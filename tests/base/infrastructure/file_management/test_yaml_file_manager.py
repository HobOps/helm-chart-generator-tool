# -*- coding: utf-8 -*-


import yaml
import unittest
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

    dumped_data1 = Mock()
    dumped_data2 = Mock()

    yaml.dump(yaml_info, dumped_data1)
    yaml.dump(my_data2, dumped_data2)

    assert my_data1["cluster"]["context"] == "default"
    assert my_data2["cluster"]["context"] == "default"

    assert dumped_data1.mock_calls[0][0] == 'write'
    assert dumped_data1.write.mock_calls.__len__() > 0
    dumped_data2.write.assert_has_calls(calls=[unittest.mock.call("cluster")])
    dumped_data2.write.assert_has_calls(calls=[unittest.mock.call("context")])
    dumped_data2.write.assert_has_calls(calls=[unittest.mock.call("namespace")])
    dumped_data2.write.assert_has_calls(calls=[unittest.mock.call("version")])
    assert True
