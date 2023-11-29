# FactFact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestations** | [**List[EntityAttestation]**](EntityAttestation.md) |  | [optional] 
**body** | **str** |  | [optional] 
**cid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**fact** | **str** |  | [optional] 
**iat** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**iss** | **str** |  | [optional] 
**jti** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fact_fact import FactFact

# TODO update the JSON string below
json = "{}"
# create an instance of FactFact from a JSON string
fact_fact_instance = FactFact.from_json(json)
# print the JSON string representation of the object
print FactFact.to_json()

# convert the object into a dict
fact_fact_dict = fact_fact_instance.to_dict()
# create an instance of FactFact from a dict
fact_fact_form_dict = fact_fact.from_dict(fact_fact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


