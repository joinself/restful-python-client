# coding: utf-8

"""
    Joinself restful-client API

    This is the api for Joinself restful client.

    The version of the OpenAPI document: 1.0
    Contact: support@swagger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.requests_api import RequestsApi


class TestRequestsApi(unittest.TestCase):
    """RequestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RequestsApi()

    def tearDown(self) -> None:
        pass

    def test_apps_app_id_requests_id_get(self) -> None:
        """Test case for apps_app_id_requests_id_get

        Get request details.
        """
        pass

    def test_apps_app_id_requests_post(self) -> None:
        """Test case for apps_app_id_requests_post

        Sends a request request.
        """
        pass


if __name__ == '__main__':
    unittest.main()