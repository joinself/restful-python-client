# AuthAuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.auth_auth_response import AuthAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAuthResponse from a JSON string
auth_auth_response_instance = AuthAuthResponse.from_json(json)
# print the JSON string representation of the object
print AuthAuthResponse.to_json()

# convert the object into a dict
auth_auth_response_dict = auth_auth_response_instance.to_dict()
# create an instance of AuthAuthResponse from a dict
auth_auth_response_form_dict = auth_auth_response.from_dict(auth_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


