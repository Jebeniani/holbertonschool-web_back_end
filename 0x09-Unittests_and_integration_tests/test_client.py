#!/usr/bin/env python3
"""Parameterizing a unit test"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"playload": True}),
        ("abc", {"playload": False}),
    ])
    @patch('Client.get_json')
    def test_org(self, org_name, expected_payload, mock_get):
        """Method to test the org method of GithubOrgClient"""
        patch.return_value = expected_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        patch.assert_called_once()
