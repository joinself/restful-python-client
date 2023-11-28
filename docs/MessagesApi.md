# openapi_client.MessagesApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_id_connections_connection_id_messages_get**](MessagesApi.md#apps_app_id_connections_connection_id_messages_get) | **GET** /apps/{app_id}/connections/{connection_id}/messages | List conversation messages.
[**apps_app_id_connections_connection_id_messages_jti_get**](MessagesApi.md#apps_app_id_connections_connection_id_messages_jti_get) | **GET** /apps/{app_id}/connections/{connection_id}/messages/{jti} | Gets a message.
[**apps_app_id_connections_connection_id_messages_jti_put**](MessagesApi.md#apps_app_id_connections_connection_id_messages_jti_put) | **PUT** /apps/{app_id}/connections/{connection_id}/messages/{jti} | Edits a message.
[**apps_app_id_connections_connection_id_messages_post**](MessagesApi.md#apps_app_id_connections_connection_id_messages_post) | **POST** /apps/{app_id}/connections/{connection_id}/messages | Sends a message.


# **apps_app_id_connections_connection_id_messages_get**
> MessageResponse apps_app_id_connections_connection_id_messages_get(app_id, connection_id, messages_since=messages_since, page=page, per_page=per_page)

List conversation messages.

List conversation messages with a specific connection.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.message_response import MessageResponse
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
    api_instance = openapi_client.MessagesApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection ID
    messages_since = 56 # int | return elements since a message id (optional)
    page = 56 # int | page number (optional)
    per_page = 56 # int | number of elements per page (optional)

    try:
        # List conversation messages.
        api_response = api_instance.apps_app_id_connections_connection_id_messages_get(app_id, connection_id, messages_since=messages_since, page=page, per_page=per_page)
        print("The response of MessagesApi->apps_app_id_connections_connection_id_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->apps_app_id_connections_connection_id_messages_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection ID | 
 **messages_since** | **int**| return elements since a message id | [optional] 
 **page** | **int**| page number | [optional] 
 **per_page** | **int**| number of elements per page | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

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

# **apps_app_id_connections_connection_id_messages_jti_get**
> MessageMessage apps_app_id_connections_connection_id_messages_jti_get(app_id, connection_id, jti)

Gets a message.

Get message details

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.message_message import MessageMessage
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
    api_instance = openapi_client.MessagesApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection id
    jti = 'jti_example' # str | Message JTI

    try:
        # Gets a message.
        api_response = api_instance.apps_app_id_connections_connection_id_messages_jti_get(app_id, connection_id, jti)
        print("The response of MessagesApi->apps_app_id_connections_connection_id_messages_jti_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->apps_app_id_connections_connection_id_messages_jti_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection id | 
 **jti** | **str**| Message JTI | 

### Return type

[**MessageMessage**](MessageMessage.md)

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

# **apps_app_id_connections_connection_id_messages_jti_put**
> MessageMessage apps_app_id_connections_connection_id_messages_jti_put(app_id, connection_id, jti, request)

Edits a message.

Sends an edited message to the specified connection.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.message_message import MessageMessage
from openapi_client.models.message_update_message_request import MessageUpdateMessageRequest
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
    api_instance = openapi_client.MessagesApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection id
    jti = 'jti_example' # str | Message jti
    request = openapi_client.MessageUpdateMessageRequest() # MessageUpdateMessageRequest | message request

    try:
        # Edits a message.
        api_response = api_instance.apps_app_id_connections_connection_id_messages_jti_put(app_id, connection_id, jti, request)
        print("The response of MessagesApi->apps_app_id_connections_connection_id_messages_jti_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->apps_app_id_connections_connection_id_messages_jti_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection id | 
 **jti** | **str**| Message jti | 
 **request** | [**MessageUpdateMessageRequest**](MessageUpdateMessageRequest.md)| message request | 

### Return type

[**MessageMessage**](MessageMessage.md)

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

# **apps_app_id_connections_connection_id_messages_post**
> MessageMessage apps_app_id_connections_connection_id_messages_post(app_id, connection_id, request)

Sends a message.

Sends a message to the specified connection.

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.message_create_message_request import MessageCreateMessageRequest
from openapi_client.models.message_message import MessageMessage
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
    api_instance = openapi_client.MessagesApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection id
    request = openapi_client.MessageCreateMessageRequest() # MessageCreateMessageRequest | message request

    try:
        # Sends a message.
        api_response = api_instance.apps_app_id_connections_connection_id_messages_post(app_id, connection_id, request)
        print("The response of MessagesApi->apps_app_id_connections_connection_id_messages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->apps_app_id_connections_connection_id_messages_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection id | 
 **request** | [**MessageCreateMessageRequest**](MessageCreateMessageRequest.md)| message request | 

### Return type

[**MessageMessage**](MessageMessage.md)

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

