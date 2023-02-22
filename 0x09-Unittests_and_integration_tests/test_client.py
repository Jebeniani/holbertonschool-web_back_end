#!/usr/bin/env python3
"""Parameterizing a unit test"""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Class to test the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, expected_payload, mock_get):
        """Method to test the org method of GithubOrgClient"""
        mock_get.return_value = expected_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
