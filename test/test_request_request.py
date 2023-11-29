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

from openapi_client.models.request_request import RequestRequest

class TestRequestRequest(unittest.TestCase):
    """RequestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestRequest:
        """Test RequestRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestRequest`
        """
        model = RequestRequest()
        if include_optional:
            return RequestRequest(
                auth = True,
                created_at = '',
                deep_link = '',
                facts = [
                    openapi_client.models.request/fact_request.request.FactRequest(
                        name = '', 
                        sources = [
                            ''
                            ], )
                    ],
                id = '',
                qr_code = '',
                resources = [
                    openapi_client.models.request/request_resource.request.RequestResource(
                        uri = '', )
                    ],
                status = '',
                typ = '',
                updated_at = ''
            )
        else:
            return RequestRequest(
        )
        """

    def testRequestRequest(self):
        """Test RequestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()