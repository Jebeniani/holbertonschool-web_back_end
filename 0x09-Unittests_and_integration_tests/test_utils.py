#!/usr/bin/env python3
"""Parameterizing a unit test"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TESTCASE"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """test method"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ method to test that a KeyError is raised properly """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])

    class TestGetJson(unittest.TestCase):
        """test function get_json"""
        @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ])
        @patch('test_utils.get_json')
        def test_get_json(self, test_url, test_payload, mock_get):
            """test method"""
            mock_get.return_value = test_payload
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

    class TestMemoize(unittest.TestCase):
        """TESTCASE"""

        def test_memoize(self):
            """TESTCASE"""
            class TestClass:
                """_summary_
                """

                def a_method(self):
                    return 42

                @memoize
                def a_property(self):
                    """property"""
                    return self.a_method()
            with patch.object(TestClass, 'a_method') as mock_method:
                instance = TestClass()
                result1 = instance.a_property
                result2 = instance.a_property

                self.assertEqual(result1, result2)
                mock_method.assert_called_once()
