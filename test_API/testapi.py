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

    # name = data['name']


    def test_request_information_about_system(self):
        pass

    def test_insert_or_update_personal_data(self):
        response = requests.put(TestPersonalData.baseUrl + 'customers/current@example.com',
                                data=json.dumps(TestPersonalData.data['addNewUser']), headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

    def test_add_and_delete_profile(self):
        response = requests.put(TestPersonalData.baseUrl + 'customers/current@example.com',
                                data=json.dumps(TestPersonalData.data['userForDel']), headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

        respD = requests.delete(TestPersonalData.baseUrl + 'customers/testadduser11@example.com',
                                data=json.dumps(TestPersonalData.data['forDelete']), headers=TestPersonalData.headers)

        data_json = json.loads(respD.text)
        assert data_json['type'] == 1
        assert respD.status_code == 200

    def test_getting_information_by_email(self):
        response = requests.get(TestPersonalData.baseUrl + 'customers/new11@example.com')
        data_json = json.loads(response.text)
        assert data_json['type'] == 1
        assert response.status_code == 200

    def test_getting_statistics_on_personal_data(self):
        response = requests.get("http://personal-data-service.dev/stats")
        data_json = json.loads(response.text)
        assert data_json['type'] == 1
        assert response.status_code == 200
