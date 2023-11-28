# openapi_client.FactsApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_id_connections_connection_id_facts_get**](FactsApi.md#apps_app_id_connections_connection_id_facts_get) | **GET** /apps/{app_id}/connections/{connection_id}/facts | List facts.
[**apps_app_id_connections_connection_id_facts_id_get**](FactsApi.md#apps_app_id_connections_connection_id_facts_id_get) | **GET** /apps/{app_id}/connections/{connection_id}/facts/{id} | Get fact details.
[**apps_app_id_connections_connection_id_facts_post**](FactsApi.md#apps_app_id_connections_connection_id_facts_post) | **POST** /apps/{app_id}/connections/{connection_id}/facts | Issues a fact.


# **apps_app_id_connections_connection_id_facts_get**
> FactResponse apps_app_id_connections_connection_id_facts_get(app_id, connection_id, page=page, per_page=per_page, source=source, fact=fact)

List facts.

List facts matching the specified filters.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.fact_response import FactResponse
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
    api_instance = openapi_client.FactsApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection id
    page = 56 # int | page number (optional)
    per_page = 56 # int | number of elements per page (optional)
    source = 56 # int | source (optional)
    fact = 56 # int | fact (optional)

    try:
        # List facts.
        api_response = api_instance.apps_app_id_connections_connection_id_facts_get(app_id, connection_id, page=page, per_page=per_page, source=source, fact=fact)
        print("The response of FactsApi->apps_app_id_connections_connection_id_facts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactsApi->apps_app_id_connections_connection_id_facts_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection id | 
 **page** | **int**| page number | [optional] 
 **per_page** | **int**| number of elements per page | [optional] 
 **source** | **int**| source | [optional] 
 **fact** | **int**| fact | [optional] 

### Return type

[**FactResponse**](FactResponse.md)

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

# **apps_app_id_connections_connection_id_facts_id_get**
> FactFact apps_app_id_connections_connection_id_facts_id_get(app_id, connection_id, id)

Get fact details.

Get fact details by fact request id.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.fact_fact import FactFact
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
    api_instance = openapi_client.FactsApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection id
    id = 56 # int | Fact request id

    try:
        # Get fact details.
        api_response = api_instance.apps_app_id_connections_connection_id_facts_id_get(app_id, connection_id, id)
        print("The response of FactsApi->apps_app_id_connections_connection_id_facts_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactsApi->apps_app_id_connections_connection_id_facts_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection id | 
 **id** | **int**| Fact request id | 

### Return type

[**FactFact**](FactFact.md)

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

# **apps_app_id_connections_connection_id_facts_post**
> apps_app_id_connections_connection_id_facts_post(app_id, connection_id, request)

Issues a fact.

Issues a fact to one of your connections.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.fact_create_fact_request_doc import FactCreateFactRequestDoc
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
    api_instance = openapi_client.FactsApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection id
    request = openapi_client.FactCreateFactRequestDoc() # FactCreateFactRequestDoc | query params

    try:
        # Issues a fact.
        api_instance.apps_app_id_connections_connection_id_facts_post(app_id, connection_id, request)
    except Exception as e:
        print("Exception when calling FactsApi->apps_app_id_connections_connection_id_facts_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection id | 
 **request** | [**FactCreateFactRequestDoc**](FactCreateFactRequestDoc.md)| query params | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

