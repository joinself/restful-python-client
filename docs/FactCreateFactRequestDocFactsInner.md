# FactCreateFactRequestDocFactsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**FactCreateFactRequestDocFactsInnerGroup**](FactCreateFactRequestDocFactsInnerGroup.md) |  | [optional] 
**key** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fact_create_fact_request_doc_facts_inner import FactCreateFactRequestDocFactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FactCreateFactRequestDocFactsInner from a JSON string
fact_create_fact_request_doc_facts_inner_instance = FactCreateFactRequestDocFactsInner.from_json(json)
# print the JSON string representation of the object
print FactCreateFactRequestDocFactsInner.to_json()

# convert the object into a dict
fact_create_fact_request_doc_facts_inner_dict = fact_create_fact_request_doc_facts_inner_instance.to_dict()
# create an instance of FactCreateFactRequestDocFactsInner from a dict
fact_create_fact_request_doc_facts_inner_form_dict = fact_create_fact_request_doc_facts_inner.from_dict(fact_create_fact_request_doc_facts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


