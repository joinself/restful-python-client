# ConnectionConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**selfid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.connection_connection import ConnectionConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConnection from a JSON string
connection_connection_instance = ConnectionConnection.from_json(json)
# print the JSON string representation of the object
print ConnectionConnection.to_json()

# convert the object into a dict
connection_connection_dict = connection_connection_instance.to_dict()
# create an instance of ConnectionConnection from a dict
connection_connection_form_dict = connection_connection.from_dict(connection_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


