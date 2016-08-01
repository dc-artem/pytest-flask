import requests
import json
import pytest
import os.path


class TestPersonalData:
    config = "adduser.json"
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), config)
    # with open('adduser.json', 'r', encoding='utf-8') as fh:
    with open(config_file) as fh:
        data = json.load(fh)
    headers = {
        'Content-type': 'application/json'
    }

    baseUrl = 'http://personal-data-service.dev/'


    #name = data['name']



    def test_request_information_about_system(self):
        pass

    def test_insert_or_update_personal_data(self):
        response = requests.put(TestPersonalData.baseUrl + 'customers/current@example.com',
                                data=json.dumps(TestPersonalData.data['addNewUser']), headers=TestPersonalData.headers)
        print("RESP:", response, "\n")
        json1 = json.loads(response.text)
        print("JSON:\n", json1)


    def test_add_and_delete_profile(self):
        response = requests.put(TestPersonalData.baseUrl + 'customers/current@example.com',
                                data=json.dumps(TestPersonalData.data['userForDel']), headers=TestPersonalData.headers)
        print(TestPersonalData.baseUrl + 'customers/testadduser2@example.com')

        print("RESP:", response, "\n")
        json1 = json.loads(response.text)
        print("JSON:\n", json1)


        # data1 = {
        #     "deletion": {
        #         "initiator": "testadduser1@example.com",
        #         "reason": "It's my desire"
        #     }
        # }
        r = requests.delete(TestPersonalData.baseUrl + 'customers/testadduser11@example.com',
                            data=json.dumps(TestPersonalData.data['forDelete']), headers=TestPersonalData.headers)
        print(r)
        print("\nSTATUS:", r.status_code)
        data_json = json.loads(r.text)
        print("RESPONSE:\n", data_json, "\n")
        assert data_json['type'] == 1

    def test_getting_information_by_email(self):
        url = "http://personal-data-service.dev/customers/new11@example.com"

        r2 = requests.get(url)
        print("\nSTATUS:", r2.status_code)
        data_json = json.loads(r2.text)
        print("RESPONSE:\n", data_json, "\n")
        assert data_json['type'] == 1


    def test_getting_statistics_on_personal_data(self):
        r = requests.get("http://personal-data-service.dev/stats")
        print("\nSTATUS:", r.status_code)
        data_json = json.loads(r.text)
        print("RESPONSE:\n", data_json, "\n")
        assert data_json['type'] == 1