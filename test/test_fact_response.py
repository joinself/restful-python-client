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

from openapi_client.models.fact_response import FactResponse

class TestFactResponse(unittest.TestCase):
    """FactResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FactResponse:
        """Test FactResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FactResponse`
        """
        model = FactResponse()
        if include_optional:
            return FactResponse(
                items = [
                    openapi_client.models.fact/fact.fact.Fact(
                        attestations = [
                            openapi_client.models.entity/attestation.entity.Attestation(
                                body = '', 
                                created_at = '', 
                                id = '', 
                                updated_at = '', 
                                value = '', )
                            ], 
                        body = '', 
                        cid = '', 
                        created_at = '', 
                        fact = '', 
                        iat = '', 
                        id = '', 
                        iss = '', 
                        jti = '', 
                        request_id = '', 
                        source = '', 
                        status = '', 
                        updated_at = '', 
                        uri = '', )
                    ],
                page = 56,
                page_count = 56,
                per_page = 56,
                total_count = 56
            )
        else:
            return FactResponse(
        )
        """

    def testFactResponse(self):
        """Test FactResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
