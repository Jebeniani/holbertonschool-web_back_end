#!/usr/bin/env python3
"""Parameterizing a unit test"""
import unittest
from mock import Mock, patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):

    def setUp(self):
        self.mock_get = Mock()
        self.test_url = 'http://example.com'
        self.test_payload = {'payload': True}

    def test_access_nested_map(self):
        """Tests access_nested_map function"""
        nested_map = {'a': {'b': {'c': 1}}}

        self.assertEqual(access_nested_map(nested_map, ['a', 'b', 'c']), 1)
        self.assertEqual(access_nested_map(nested_map, ['a', 'b']), {'c': 1})
        self.assertRaises(KeyError, access_nested_map,
                          nested_map, ['d', 'e', 'f'])

    def test_get_json(self):
        """Tests get_json function"""
        self.mock_get.return_value.json.return_value = {"payload": True}
        with patch('requests.get', self.mock_get):
            response = get_json(self.test_url)

        self.assertEqual(response, self.test_payload)
