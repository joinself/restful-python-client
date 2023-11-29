# RequestFactRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sources** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.request_fact_request import RequestFactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFactRequest from a JSON string
request_fact_request_instance = RequestFactRequest.from_json(json)
# print the JSON string representation of the object
print RequestFactRequest.to_json()

# convert the object into a dict
request_fact_request_dict = request_fact_request_instance.to_dict()
# create an instance of RequestFactRequest from a dict
request_fact_request_form_dict = request_fact_request.from_dict(request_fact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


