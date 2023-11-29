# self-restful-client-python-openapi
This is the api for Joinself restful client.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://www.swagger.io/support](http://www.swagger.io/support)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
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
    api_instance = openapi_client.AppsApi(api_client)

    try:
        # List apps.
        api_response = api_instance.apps_get()
        print("The response of AppsApi->apps_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->apps_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:8080/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppsApi* | [**apps_get**](docs/AppsApi.md#apps_get) | **GET** /apps | List apps.
*ConnectionsApi* | [**apps_app_id_connections_get**](docs/ConnectionsApi.md#apps_app_id_connections_get) | **GET** /apps/{app_id}/connections | List connections.
*ConnectionsApi* | [**apps_app_id_connections_id_delete**](docs/ConnectionsApi.md#apps_app_id_connections_id_delete) | **DELETE** /apps/{app_id}/connections/{id} | Deletes an existing connection.
*ConnectionsApi* | [**apps_app_id_connections_id_get**](docs/ConnectionsApi.md#apps_app_id_connections_id_get) | **GET** /apps/{app_id}/connections/{id} | Get connection details.
*ConnectionsApi* | [**apps_app_id_connections_id_put**](docs/ConnectionsApi.md#apps_app_id_connections_id_put) | **PUT** /apps/{app_id}/connections/{id} | Updates a connection.
*ConnectionsApi* | [**apps_app_id_connections_post**](docs/ConnectionsApi.md#apps_app_id_connections_post) | **POST** /apps/{app_id}/connections | Creates a new connection.
*FactsApi* | [**apps_app_id_connections_connection_id_facts_get**](docs/FactsApi.md#apps_app_id_connections_connection_id_facts_get) | **GET** /apps/{app_id}/connections/{connection_id}/facts | List facts.
*FactsApi* | [**apps_app_id_connections_connection_id_facts_id_get**](docs/FactsApi.md#apps_app_id_connections_connection_id_facts_id_get) | **GET** /apps/{app_id}/connections/{connection_id}/facts/{id} | Get fact details.
*FactsApi* | [**apps_app_id_connections_connection_id_facts_post**](docs/FactsApi.md#apps_app_id_connections_connection_id_facts_post) | **POST** /apps/{app_id}/connections/{connection_id}/facts | Issues a fact.
*HealthcheckApi* | [**healthcheck_get**](docs/HealthcheckApi.md#healthcheck_get) | **GET** /healthcheck | healthcheck endpoint
*LoginApi* | [**login_post**](docs/LoginApi.md#login_post) | **POST** /login | Authenticate.
*MessagesApi* | [**apps_app_id_connections_connection_id_messages_get**](docs/MessagesApi.md#apps_app_id_connections_connection_id_messages_get) | **GET** /apps/{app_id}/connections/{connection_id}/messages | List conversation messages.
*MessagesApi* | [**apps_app_id_connections_connection_id_messages_jti_get**](docs/MessagesApi.md#apps_app_id_connections_connection_id_messages_jti_get) | **GET** /apps/{app_id}/connections/{connection_id}/messages/{jti} | Gets a message.
*MessagesApi* | [**apps_app_id_connections_connection_id_messages_jti_put**](docs/MessagesApi.md#apps_app_id_connections_connection_id_messages_jti_put) | **PUT** /apps/{app_id}/connections/{connection_id}/messages/{jti} | Edits a message.
*MessagesApi* | [**apps_app_id_connections_connection_id_messages_post**](docs/MessagesApi.md#apps_app_id_connections_connection_id_messages_post) | **POST** /apps/{app_id}/connections/{connection_id}/messages | Sends a message.
*NotificationsApi* | [**apps_app_id_connections_connection_id_notify_post**](docs/NotificationsApi.md#apps_app_id_connections_connection_id_notify_post) | **POST** /apps/{app_id}/connections/{connection_id}/notify | Sends a system notification.
*RequestsApi* | [**apps_app_id_requests_id_get**](docs/RequestsApi.md#apps_app_id_requests_id_get) | **GET** /apps/{app_id}/requests/{id} | Get request details.
*RequestsApi* | [**apps_app_id_requests_post**](docs/RequestsApi.md#apps_app_id_requests_post) | **POST** /apps/{app_id}/requests | Sends a request request.


## Documentation For Models

 - [AppApp](docs/AppApp.md)
 - [AppResponse](docs/AppResponse.md)
 - [AuthAuthRequest](docs/AuthAuthRequest.md)
 - [AuthAuthResponse](docs/AuthAuthResponse.md)
 - [ConnectionConnection](docs/ConnectionConnection.md)
 - [ConnectionCreateConnectionRequest](docs/ConnectionCreateConnectionRequest.md)
 - [ConnectionResponse](docs/ConnectionResponse.md)
 - [ConnectionUpdateConnectionRequest](docs/ConnectionUpdateConnectionRequest.md)
 - [EntityAttestation](docs/EntityAttestation.md)
 - [FactCreateFactRequestDoc](docs/FactCreateFactRequestDoc.md)
 - [FactCreateFactRequestDocFactsInner](docs/FactCreateFactRequestDocFactsInner.md)
 - [FactCreateFactRequestDocFactsInnerGroup](docs/FactCreateFactRequestDocFactsInnerGroup.md)
 - [FactFact](docs/FactFact.md)
 - [FactResponse](docs/FactResponse.md)
 - [MessageCreateMessageRequest](docs/MessageCreateMessageRequest.md)
 - [MessageMessage](docs/MessageMessage.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [MessageUpdateMessageRequest](docs/MessageUpdateMessageRequest.md)
 - [NotificationSystemNotificationData](docs/NotificationSystemNotificationData.md)
 - [NotificationSystemNotificationDataMetadata](docs/NotificationSystemNotificationDataMetadata.md)
 - [NotificationSystemNotificationDataNotification](docs/NotificationSystemNotificationDataNotification.md)
 - [RequestCreateRequest](docs/RequestCreateRequest.md)
 - [RequestFactRequest](docs/RequestFactRequest.md)
 - [RequestRequest](docs/RequestRequest.md)
 - [RequestRequestResource](docs/RequestRequestResource.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@swagger.io


