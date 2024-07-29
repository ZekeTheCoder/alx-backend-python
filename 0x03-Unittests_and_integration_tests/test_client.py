#!/usr/bin/env python3
""" Mocking a property """

from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock
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
        client = GithubOrgClient(org_name)
        result = client.org
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"name": org_name})

    def test_public_repos_url(self):
        """Test the GithubOrgClient._public_repos_url function"""

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock,
                          return_value={"repos_url": "Test value"}
                          ) as mock_org:
            mock_property = {"repos_url": "Test value"}
            client = GithubOrgClient(mock_property.get("repos_url"))
            result = client._public_repos_url

            self.assertEqual(result, mock_org.return_value.get("repos_url"))
            mock_org.assert_called_once
