# openapi_client.HealthcheckApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck_get**](HealthcheckApi.md#healthcheck_get) | **GET** /healthcheck | healthcheck endpoint


# **healthcheck_get**
> str healthcheck_get()

healthcheck endpoint

check the service is up and running

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.HealthcheckApi(api_client)

    try:
        # healthcheck endpoint
        api_response = api_instance.healthcheck_get()
        print("The response of HealthcheckApi->healthcheck_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthcheckApi->healthcheck_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

