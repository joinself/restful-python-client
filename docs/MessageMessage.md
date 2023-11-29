# MessageMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**cid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**iat** | **str** |  | [optional] 
**iss** | **str** |  | [optional] 
**jti** | **str** |  | [optional] 
**rid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.message_message import MessageMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MessageMessage from a JSON string
message_message_instance = MessageMessage.from_json(json)
# print the JSON string representation of the object
print MessageMessage.to_json()

# convert the object into a dict
message_message_dict = message_message_instance.to_dict()
# create an instance of MessageMessage from a dict
message_message_form_dict = message_message.from_dict(message_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


