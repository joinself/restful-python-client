# RequestCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | **str** |  | [optional] 
**connection_self_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**facts** | [**List[RequestFactRequest]**](RequestFactRequest.md) |  | [optional] 
**out_of_band** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.request_create_request import RequestCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCreateRequest from a JSON string
request_create_request_instance = RequestCreateRequest.from_json(json)
# print the JSON string representation of the object
print RequestCreateRequest.to_json()

# convert the object into a dict
request_create_request_dict = request_create_request_instance.to_dict()
# create an instance of RequestCreateRequest from a dict
request_create_request_form_dict = request_create_request.from_dict(request_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


