#!/usr/bin/env python3
""" Integration test: fixtures """

from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json", return_value=[{"name": "Test value"}])
    def test_public_repos(self, mock):
        """Test GithubOrgClient.public_rep function"""

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/"
                          ) as mock_public_repos_url:
            client = GithubOrgClient("Test value")
            result = client.public_repos()

            self.assertEqual(result, ["Test value"])
            mock.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license function"""

        client = GithubOrgClient("Test value")
        result = client.has_license(repo, license_key)
        self.assertEqual(expected, result)


@parameterized_class(("org_payload", "repos_payload", "expected_repos",
                     "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(TestCase):
    """Test the GithubOrgClient.public_repos method in an integration test"""

    @classmethod
    def setUpClass(cls):
        """Set up the patcher for requests.get"""
        # Prepare mock responses
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        # Patch requests.get
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        # Configure side effect for the mock
        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()
