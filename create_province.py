# refer to: https://developers.hubspot.com/docs/api/crm/properties
import requests
import json
import pandas as pd

# choose whether you want to create the property in contacts or companies
objectType = "COMPANIES"
# objectType = "CONTACTS"
# objectType = "DEALS"

# HubSpot API endpoint
url = f"https://api.hubapi.com/crm/v3/properties/{objectType}"

# insert here your HubSpot API KEY
querystring = {"hapikey": "<YOUR-API-KEY>"}

df = pd.read_json('./province.json')
df = df.drop(columns=['regione']).rename({
    "nome": "label",
    "sigla": "value"
},
                                         axis=1)
df['description'] = ""
df['displayOrder'] = df.index + 1

options = json.loads(df.to_json(index=False, orient='table'))['data']

# choose the Property Group where you want to insert the new property:
# default to comapnyinformation for COMPANIES, contactinformation for CONTACTS
groupName = "companyinformation"  # "contactinformation"

# here you can edit anything at your needs
payload = {
    "hidden": False,
    "groupName": groupName,
    "displayOrder": 5,
    "label": "Provincia",
    "hasUniqueValue": False,
    "type": "enumeration",
    "fieldType": "select",
    "formField": True,
    "name": "provincia",
    "description": "Provincia Italiana",
    "options": options
}

headers = {'accept': "application/json", 'content-type': "application/json"}

response = requests.request("POST",
                            url,
                            data=json.dumps(payload),
                            headers=headers,
                            params=querystring)

# response = requests.request("GET",
#                             url,
#                             headers=headers,
#                             params=querystring)

print(response.text)
