# NotificationSystemNotificationDataNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.notification_system_notification_data_notification import NotificationSystemNotificationDataNotification

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSystemNotificationDataNotification from a JSON string
notification_system_notification_data_notification_instance = NotificationSystemNotificationDataNotification.from_json(json)
# print the JSON string representation of the object
print NotificationSystemNotificationDataNotification.to_json()

# convert the object into a dict
notification_system_notification_data_notification_dict = notification_system_notification_data_notification_instance.to_dict()
# create an instance of NotificationSystemNotificationDataNotification from a dict
notification_system_notification_data_notification_form_dict = notification_system_notification_data_notification.from_dict(notification_system_notification_data_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


