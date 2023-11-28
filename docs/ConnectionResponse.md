# ConnectionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ConnectionConnection]**](ConnectionConnection.md) |  | [optional] 
**page** | **int** |  | [optional] 
**page_count** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.connection_response import ConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionResponse from a JSON string
connection_response_instance = ConnectionResponse.from_json(json)
# print the JSON string representation of the object
print ConnectionResponse.to_json()

# convert the object into a dict
connection_response_dict = connection_response_instance.to_dict()
# create an instance of ConnectionResponse from a dict
connection_response_form_dict = connection_response.from_dict(connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


