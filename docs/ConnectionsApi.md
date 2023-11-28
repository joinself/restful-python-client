# openapi_client.ConnectionsApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_id_connections_get**](ConnectionsApi.md#apps_app_id_connections_get) | **GET** /apps/{app_id}/connections | List connections.
[**apps_app_id_connections_id_delete**](ConnectionsApi.md#apps_app_id_connections_id_delete) | **DELETE** /apps/{app_id}/connections/{id} | Deletes an existing connection.
[**apps_app_id_connections_id_get**](ConnectionsApi.md#apps_app_id_connections_id_get) | **GET** /apps/{app_id}/connections/{id} | Get connection details.
[**apps_app_id_connections_id_put**](ConnectionsApi.md#apps_app_id_connections_id_put) | **PUT** /apps/{app_id}/connections/{id} | Updates a connection.
[**apps_app_id_connections_post**](ConnectionsApi.md#apps_app_id_connections_post) | **POST** /apps/{app_id}/connections | Creates a new connection.


# **apps_app_id_connections_get**
> ConnectionResponse apps_app_id_connections_get(app_id, page=page, per_page=per_page)

List connections.

List connections matching the specified filters.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.connection_response import ConnectionResponse
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
    api_instance = openapi_client.ConnectionsApi(api_client)
    app_id = 'app_id_example' # str | App id
    page = 56 # int | page number (optional)
    per_page = 56 # int | number of elements per page (optional)

    try:
        # List connections.
        api_response = api_instance.apps_app_id_connections_get(app_id, page=page, per_page=per_page)
        print("The response of ConnectionsApi->apps_app_id_connections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->apps_app_id_connections_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **page** | **int**| page number | [optional] 
 **per_page** | **int**| number of elements per page | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

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

# **apps_app_id_connections_id_delete**
> ConnectionConnection apps_app_id_connections_id_delete(app_id, id, request)

Deletes an existing connection.

Deletes an existing connection and sends a request for public information and avoids incoming comms from that connection.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.connection_connection import ConnectionConnection
from openapi_client.models.connection_create_connection_request import ConnectionCreateConnectionRequest
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
    api_instance = openapi_client.ConnectionsApi(api_client)
    app_id = 'app_id_example' # str | App id
    id = 56 # int | current connection id
    request = openapi_client.ConnectionCreateConnectionRequest() # ConnectionCreateConnectionRequest | query params

    try:
        # Deletes an existing connection.
        api_response = api_instance.apps_app_id_connections_id_delete(app_id, id, request)
        print("The response of ConnectionsApi->apps_app_id_connections_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->apps_app_id_connections_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **id** | **int**| current connection id | 
 **request** | [**ConnectionCreateConnectionRequest**](ConnectionCreateConnectionRequest.md)| query params | 

### Return type

[**ConnectionConnection**](ConnectionConnection.md)

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

# **apps_app_id_connections_id_get**
> ConnectionConnection apps_app_id_connections_id_get(app_id, id)

Get connection details.

Get connection details by selfID.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.connection_connection import ConnectionConnection
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
    api_instance = openapi_client.ConnectionsApi(api_client)
    app_id = 'app_id_example' # str | App id
    id = 56 # int | current connection id

    try:
        # Get connection details.
        api_response = api_instance.apps_app_id_connections_id_get(app_id, id)
        print("The response of ConnectionsApi->apps_app_id_connections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->apps_app_id_connections_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **id** | **int**| current connection id | 

### Return type

[**ConnectionConnection**](ConnectionConnection.md)

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

# **apps_app_id_connections_id_put**
> ConnectionConnection apps_app_id_connections_id_put(app_id, id, request)

Updates a connection.

Updates the properties of an existing connection..

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.connection_connection import ConnectionConnection
from openapi_client.models.connection_update_connection_request import ConnectionUpdateConnectionRequest
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
    api_instance = openapi_client.ConnectionsApi(api_client)
    app_id = 'app_id_example' # str | App id
    id = 56 # int | current connection id
    request = openapi_client.ConnectionUpdateConnectionRequest() # ConnectionUpdateConnectionRequest | query params

    try:
        # Updates a connection.
        api_response = api_instance.apps_app_id_connections_id_put(app_id, id, request)
        print("The response of ConnectionsApi->apps_app_id_connections_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->apps_app_id_connections_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **id** | **int**| current connection id | 
 **request** | [**ConnectionUpdateConnectionRequest**](ConnectionUpdateConnectionRequest.md)| query params | 

### Return type

[**ConnectionConnection**](ConnectionConnection.md)

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

# **apps_app_id_connections_post**
> ConnectionConnection apps_app_id_connections_post(app_id, request)

Creates a new connection.

Creates a new connection and sends a request for public information.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.connection_connection import ConnectionConnection
from openapi_client.models.connection_create_connection_request import ConnectionCreateConnectionRequest
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
    api_instance = openapi_client.ConnectionsApi(api_client)
    app_id = 'app_id_example' # str | App id
    request = openapi_client.ConnectionCreateConnectionRequest() # ConnectionCreateConnectionRequest | query params

    try:
        # Creates a new connection.
        api_response = api_instance.apps_app_id_connections_post(app_id, request)
        print("The response of ConnectionsApi->apps_app_id_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->apps_app_id_connections_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **request** | [**ConnectionCreateConnectionRequest**](ConnectionCreateConnectionRequest.md)| query params | 

### Return type

[**ConnectionConnection**](ConnectionConnection.md)

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

