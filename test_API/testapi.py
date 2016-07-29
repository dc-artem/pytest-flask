import requests
import json


def test_info():
    url = "http://personal-data-service.dev/customers/test@tets.ru"
    r2 = requests.get(url)
    print(r2)
    print("\nSTATUS:", r2.status_code)
    data_json = json.loads(r2.text)
    print("RESPONSE:\n", data_json, "\n")
    assert data_json['type'] == 1


def test_requests():
    r = requests.get("http://personal-data-service.dev/stats")
    print("\nSTATUS:", r.status_code)
    data_json = json.loads(r.text)
    print("RESPONSE:\n", data_json, "\n")
    assert data_json['type'] == 1


def test_delete_profile():
    headers = {
        'Content-type': 'application/json'
    }

    data = {
        "deletion": {
            "initiator": "current333@example.com",
            "reason": "It's my desire"
        }
    }

    url = "http://personal-data-service.dev/customers/current333@example.com"
    r = requests.delete(url, data=json.dumps(data), headers=headers)
    print("\nSTATUS:", r.status_code)
    data_json = json.loads(r.text)
    print("RESPONSE:\n", data_json, "\n")
    assert data_json['type'] == 1

def test_email_info():

    headers = {
        'Content-type':'application/json'
    }
    data = {
        "customer": {
            "email": "current@example.com"
        },
        "customerInfo": {
            "email": "current@example.com",
            "firstName": "Olaf",
            "lastName": "Henderson",
            "birthDate": "1990-12-12",
            "mobilePhoneCountryCode": "+49",
            "mobilePhoneNumber": "123-44-66"
        },
        "customerAddress": {
            "cityId": 123,
            "areaId": 321,
            "addressLine1": "Arbat",
            "addressLine2": "Arbatskaya",
            "addressLine3": "",
            "addressLine4": "",
            "addressLine5": "",
            "addressOther": "",
            "room": "1",
            "flatNumber": "12",
            "structure": "1F",
            "building": "B",
            "intercom": "111",
            "entrance": "222",
            "floor": "10",
            "district": "Northern",
            "postcode": "111222",
            "latitude": "22.265033",
            "longitude": "114.153"
        }

    }
    url = 'http://personal-data-service.dev/customers'
    response = requests.put(url, data=json.dumps(data), headers=headers)
    print("RESP:", response, "\n")
    json1 = json.loads(response.text)
    print("JSON:\n", json1)
