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
import datetime

from openapi_client.models.connection_update_connection_request import ConnectionUpdateConnectionRequest

class TestConnectionUpdateConnectionRequest(unittest.TestCase):
    """ConnectionUpdateConnectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionUpdateConnectionRequest:
        """Test ConnectionUpdateConnectionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionUpdateConnectionRequest`
        """
        model = ConnectionUpdateConnectionRequest()
        if include_optional:
            return ConnectionUpdateConnectionRequest(
                name = ''
            )
        else:
            return ConnectionUpdateConnectionRequest(
        )
        """

    def testConnectionUpdateConnectionRequest(self):
        """Test ConnectionUpdateConnectionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
