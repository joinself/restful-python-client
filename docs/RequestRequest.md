# RequestRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**deep_link** | **str** |  | [optional] 
**facts** | [**List[RequestFactRequest]**](RequestFactRequest.md) |  | [optional] 
**id** | **str** |  | [optional] 
**qr_code** | **str** |  | [optional] 
**resources** | [**List[RequestRequestResource]**](RequestRequestResource.md) |  | [optional] 
**status** | **str** |  | [optional] 
**typ** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.request_request import RequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRequest from a JSON string
request_request_instance = RequestRequest.from_json(json)
# print the JSON string representation of the object
print RequestRequest.to_json()

# convert the object into a dict
request_request_dict = request_request_instance.to_dict()
# create an instance of RequestRequest from a dict
request_request_form_dict = request_request.from_dict(request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


