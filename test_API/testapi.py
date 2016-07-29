import requests
import json
from flask import Flask
#from flask import Response, json
from flask.testing import FlaskClient




# app = Flask(__name__)
#
# def test_app(client):
#     response = client.get('http://personal-data-service.dev' + 'stats/')
#     assert response.status_code == 200
#     assert isinstance(response, Response)
#
#     json_data = json.loads(response.data.decode('utf-8'))
#     print(json_data)
#     assert isinstance(json_data, list)
#     print(json_data)
#     # assert response.json['type'] == '1'


r = requests.get("http://personal-data-service.dev/stats")


def test_requests():
    print("\nSTATUS:", r.status_code)
    data_json = json.loads(r.text)
    print("RESPONSE:\n", data_json)
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
