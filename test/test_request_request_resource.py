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

from openapi_client.models.request_request_resource import RequestRequestResource

class TestRequestRequestResource(unittest.TestCase):
    """RequestRequestResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestRequestResource:
        """Test RequestRequestResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestRequestResource`
        """
        model = RequestRequestResource()
        if include_optional:
            return RequestRequestResource(
                uri = ''
            )
        else:
            return RequestRequestResource(
        )
        """

    def testRequestRequestResource(self):
        """Test RequestRequestResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
