# openapi_client.LoginApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_post**](LoginApi.md#login_post) | **POST** /login | Authenticate.


# **login_post**
> AuthAuthResponse login_post(request)

Authenticate.

Get a temporary JWT token to interact with the api.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.auth_auth_request import AuthAuthRequest
from openapi_client.models.auth_auth_response import AuthAuthResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LoginApi(api_client)
    request = openapi_client.AuthAuthRequest() # AuthAuthRequest | Self ID

    try:
        # Authenticate.
        api_response = api_instance.login_post(request)
        print("The response of LoginApi->login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AuthAuthRequest**](AuthAuthRequest.md)| Self ID | 

### Return type

[**AuthAuthResponse**](AuthAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

