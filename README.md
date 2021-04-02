# Add Italian Province to [HubSpot](https://www.hubspot.com/)

This is a simple python script which adds Italian "Province" to Hubspot CRM which is otherwhise a lenghty manul task as italian Province are not in HubSpot by default.

The province.json file has been taken from [stockmind/province-italia.json](https://gist.github.com/stockmind/8bcbbf9ac41bc196401b96084ec8c5d3).

To create the province property just run the following code:

```python
import create_province

API_KEY = "<YOUR HUBSPOT API KEY>"
object_type = "CONTACTS"
group_name = "contactinformation"
display_order = 2
# you can customize other options such as hasUniqueValue and other:
# see create_province.py

response = create_province.create_hubspot_provincia(API_KEY, object_type,
                                                    group_name, display_order)

print(response.text)
```

This will create a dropdown select property labeld *Provincia* in your Contacts in the Contact Information property group.
You can also add the property to COMPANIES and DEALS by changing the object_type and group_name variables.
Other options can be customized such as *hasUniqueValue* and *description*. Please refer to the file create_province.py for more about this.

Each Provincia will be created like the example below:

Label -> Agrigento

Value -> AG

The value displayed in the contact page is the label hence the whole name of the Provinvcia will be displayed.
