import requests
import json


def read_province():
    with open("./province.json", "r") as json_file:
        data = json.load(json_file)
    return data


def transform_data():
    data = read_province()
    for i, item in enumerate(data):
        item["description"] = ""
        item["displayOrder"] = i + 1
        item["label"] = item.pop("nome")
        item["value"] = item.pop("sigla")
        item.pop("regione")
    return data


def generate_payload(group_name,
                     display_order,
                     has_unique_value=False,
                     form_field=True,
                     name="provincia",
                     label="Provincia",
                     description="Provincia Italiana"):
    payload = {
        "hidden": False,
        "groupName": group_name,
        "displayOrder": display_order,
        "label": "Provincia",
        "hasUniqueValue": has_unique_value,
        "type": "enumeration",
        "fieldType": "select",
        "formField": form_field,
        "name": name,
        "description": description,
        "options": transform_data()
    }
    return payload


def create_hubspot_provincia(API_KEY, object_type, group_name, display_order,
                             **kwargs):
    """
    Create Provincia Property in HubSpot CRM.

    Parameters
    ----------
    API_KEY : string
        Your HubSpot API KEY.
    object_type : string
        One of 'COMPANIES', 'CONTACTS' or 'DEALS'.
    group_name :  string
        Property Group e.g. 'contactinformation'.
    display_order : integer
        Properties are displayed in order starting with
        the lowest positive integer value.
        Values of -1 will cause the property
        to be displayed after any positive values.
    has_unique_value : bool, default False
        Whether or not the property's value must be unique.
        Once set, this can't be changed.
    form_field : bool, default True
        Whether or not the property can be used in a HubSpot form.
    name : string, default 'provincia'
        The internal property name, which must be used
        when referencing the property via the API.
    label : string, default 'Provincia'
        A human-readable property label that will be shown in HubSpot.
    description : string, default 'Provincia Italiana'
        A description of the property
        that will be shown as help text in HubSpot.

    Returns
    -------
    Response object.
    """
    payload = generate_payload(group_name, display_order, **kwargs)
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
    }
    url = "https://api.hubapi.com/crm/v3/properties/{}".format(object_type)
    querystring = {"hapikey": "{}".format(API_KEY)}
    return requests.request("POST",
                            url,
                            data=json.dumps(payload),
                            headers=headers,
                            params=querystring)
