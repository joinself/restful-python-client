# EntityAttestation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.entity_attestation import EntityAttestation

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAttestation from a JSON string
entity_attestation_instance = EntityAttestation.from_json(json)
# print the JSON string representation of the object
print EntityAttestation.to_json()

# convert the object into a dict
entity_attestation_dict = entity_attestation_instance.to_dict()
# create an instance of EntityAttestation from a dict
entity_attestation_form_dict = entity_attestation.from_dict(entity_attestation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


