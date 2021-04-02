# refer to: https://developers.hubspot.com/docs/api/crm/properties
import create_province

API_KEY = "<YOUR HUBSPOT API KEY>"
object_type = "CONTACTS"
group_name = "contactinformation"
display_order = 2

response = create_province.create_hubspot_provincia(API_KEY, object_type,
                                                    group_name, display_order)

print(response.text)
