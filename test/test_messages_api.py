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

from openapi_client.api.messages_api import MessagesApi


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MessagesApi()

    def tearDown(self) -> None:
        pass

    def test_apps_app_id_connections_connection_id_messages_get(self) -> None:
        """Test case for apps_app_id_connections_connection_id_messages_get

        List conversation messages.
        """
        pass

    def test_apps_app_id_connections_connection_id_messages_jti_get(self) -> None:
        """Test case for apps_app_id_connections_connection_id_messages_jti_get

        Gets a message.
        """
        pass

    def test_apps_app_id_connections_connection_id_messages_jti_put(self) -> None:
        """Test case for apps_app_id_connections_connection_id_messages_jti_put

        Edits a message.
        """
        pass

    def test_apps_app_id_connections_connection_id_messages_post(self) -> None:
        """Test case for apps_app_id_connections_connection_id_messages_post

        Sends a message.
        """
        pass


if __name__ == '__main__':
    unittest.main()
