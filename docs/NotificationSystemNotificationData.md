# NotificationSystemNotificationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**NotificationSystemNotificationDataMetadata**](NotificationSystemNotificationDataMetadata.md) |  | [optional] 
**notification** | [**NotificationSystemNotificationDataNotification**](NotificationSystemNotificationDataNotification.md) |  | [optional] 

## Example

```python
from openapi_client.models.notification_system_notification_data import NotificationSystemNotificationData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSystemNotificationData from a JSON string
notification_system_notification_data_instance = NotificationSystemNotificationData.from_json(json)
# print the JSON string representation of the object
print NotificationSystemNotificationData.to_json()

# convert the object into a dict
notification_system_notification_data_dict = notification_system_notification_data_instance.to_dict()
# create an instance of NotificationSystemNotificationData from a dict
notification_system_notification_data_form_dict = notification_system_notification_data.from_dict(notification_system_notification_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


