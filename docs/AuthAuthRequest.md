# AuthAuthRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.auth_auth_request import AuthAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAuthRequest from a JSON string
auth_auth_request_instance = AuthAuthRequest.from_json(json)
# print the JSON string representation of the object
print AuthAuthRequest.to_json()

# convert the object into a dict
auth_auth_request_dict = auth_auth_request_instance.to_dict()
# create an instance of AuthAuthRequest from a dict
auth_auth_request_form_dict = auth_auth_request.from_dict(auth_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


