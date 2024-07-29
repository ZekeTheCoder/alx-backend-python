#!/usr/bin/env python3
""" Parameterize and patch as decorators """

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ Test client.GithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """ Test that GithubOrgClient.org returns the correct output """
        mock.return_value = {"name": org_name}
        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)
        result = client.org
        # Check that get_json was called exactly once with the expected URL
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        # Check that the returned result is as expected
        self.assertEqual(result, {"name": org_name})
