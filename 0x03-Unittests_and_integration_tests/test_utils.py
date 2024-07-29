#!/usr/bin/env python3
""" Parameterize and patch """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test utils.access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test access_nested_map function raises KeyError """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """Test utils.get_json function with mocked HTTP requests"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Method to test that utils.get_json returns the expected result """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test utils.memoize function/decorator"""

    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result is
            returned but a_method is only called once using assert_called_once
        """

        class TestClass:
            """Test class with memoization"""

            def a_method(self):
                """Method that returns an instance of memoize class"""
                return 42

            @memoize
            def a_property(self):
                """Method that defines a property instance of memoize"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            test_class = TestClass()

            test_class.a_property
            test_class.a_property

            mock.assert_called_once
