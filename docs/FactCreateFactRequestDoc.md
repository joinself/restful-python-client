# FactCreateFactRequestDoc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facts** | [**List[FactCreateFactRequestDocFactsInner]**](FactCreateFactRequestDocFactsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.fact_create_fact_request_doc import FactCreateFactRequestDoc

# TODO update the JSON string below
json = "{}"
# create an instance of FactCreateFactRequestDoc from a JSON string
fact_create_fact_request_doc_instance = FactCreateFactRequestDoc.from_json(json)
# print the JSON string representation of the object
print FactCreateFactRequestDoc.to_json()

# convert the object into a dict
fact_create_fact_request_doc_dict = fact_create_fact_request_doc_instance.to_dict()
# create an instance of FactCreateFactRequestDoc from a dict
fact_create_fact_request_doc_form_dict = fact_create_fact_request_doc.from_dict(fact_create_fact_request_doc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


