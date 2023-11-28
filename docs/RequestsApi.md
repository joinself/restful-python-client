# openapi_client.RequestsApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_id_requests_id_get**](RequestsApi.md#apps_app_id_requests_id_get) | **GET** /apps/{app_id}/requests/{id} | Get request details.
[**apps_app_id_requests_post**](RequestsApi.md#apps_app_id_requests_post) | **POST** /apps/{app_id}/requests | Sends a request request.


# **apps_app_id_requests_id_get**
> RequestRequest apps_app_id_requests_id_get(app_id, id)

Get request details.

Get request details by request request id.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.request_request import RequestRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RequestsApi(api_client)
    app_id = 'app_id_example' # str | App id
    id = 56 # int | Request request id

    try:
        # Get request details.
        api_response = api_instance.apps_app_id_requests_id_get(app_id, id)
        print("The response of RequestsApi->apps_app_id_requests_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->apps_app_id_requests_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **id** | **int**| Request request id | 

### Return type

[**RequestRequest**](RequestRequest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_id_requests_post**
> RequestRequest apps_app_id_requests_post(app_id, request)

Sends a request request.

Sends a request request to the specified self user.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.request_create_request import RequestCreateRequest
from openapi_client.models.request_request import RequestRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RequestsApi(api_client)
    app_id = 'app_id_example' # str | App id
    request = openapi_client.RequestCreateRequest() # RequestCreateRequest | query params

    try:
        # Sends a request request.
        api_response = api_instance.apps_app_id_requests_post(app_id, request)
        print("The response of RequestsApi->apps_app_id_requests_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->apps_app_id_requests_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **request** | [**RequestCreateRequest**](RequestCreateRequest.md)| query params | 

### Return type

[**RequestRequest**](RequestRequest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

