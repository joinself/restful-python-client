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

from openapi_client.models.message_response import MessageResponse

class TestMessageResponse(unittest.TestCase):
    """MessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageResponse:
        """Test MessageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageResponse`
        """
        model = MessageResponse()
        if include_optional:
            return MessageResponse(
                items = [
                    openapi_client.models.message/message.message.Message(
                        body = '', 
                        cid = '', 
                        created_at = '', 
                        iat = '', 
                        iss = '', 
                        jti = '', 
                        rid = '', 
                        updated_at = '', )
                    ],
                page = 56,
                page_count = 56,
                per_page = 56,
                total_count = 56
            )
        else:
            return MessageResponse(
        )
        """

    def testMessageResponse(self):
        """Test MessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
