#!/usr/bin/env python3
"""Parameterizing a unit test"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the GithubOrgClient class"""

    @parameterized.expand([
        ("google"), ("abc")
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, expected_payload, mock_get):
        """Method to test the org method of GithubOrgClient"""
        mock_get.return_value = expected_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
