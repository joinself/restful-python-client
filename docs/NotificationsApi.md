# openapi_client.NotificationsApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_id_connections_connection_id_notify_post**](NotificationsApi.md#apps_app_id_connections_connection_id_notify_post) | **POST** /apps/{app_id}/connections/{connection_id}/notify | Sends a system notification.


# **apps_app_id_connections_connection_id_notify_post**
> apps_app_id_connections_connection_id_notify_post(app_id, connection_id, request)

Sends a system notification.

Sends a system notification to the given connection

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.notification_system_notification_data import NotificationSystemNotificationData
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
    api_instance = openapi_client.NotificationsApi(api_client)
    app_id = 'app_id_example' # str | App id
    connection_id = 'connection_id_example' # str | Connection id
    request = openapi_client.NotificationSystemNotificationData() # NotificationSystemNotificationData | system notification

    try:
        # Sends a system notification.
        api_instance.apps_app_id_connections_connection_id_notify_post(app_id, connection_id, request)
    except Exception as e:
        print("Exception when calling NotificationsApi->apps_app_id_connections_connection_id_notify_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| App id | 
 **connection_id** | **str**| Connection id | 
 **request** | [**NotificationSystemNotificationData**](NotificationSystemNotificationData.md)| system notification | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

