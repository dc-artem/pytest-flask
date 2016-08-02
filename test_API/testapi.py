import requests
import json
import pytest
import os.path
from test_API.mail_random_generator import generate_random_email

class TestPersonalData:

    email = generate_random_email(7)
    config = "adduser.json"
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), config)
    # with open('adduser.json', 'r', encoding='utf-8') as fh:
    with open(config_file) as fh:
        data = json.load(fh)
    headers = {
        'Content-type': 'application/json'
    }
    baseUrlCustomers = data['urls']["baseUrlCustomers"]
    baseUrl = data['urls']["baseUrl"]
    emailjson = data['addNewUser']['customerInfo']['email']
    print("\nemailjson:", emailjson)
    emailjson = {'email': email}
    print("\nemailjson:", emailjson)
    print(email)



    def request_information_about_system(self):
        pass




    def test_insert_personal_data(self):
        addUserData = TestPersonalData.data['addNewUser']
        addUserData['customerInfo']['email'] = TestPersonalData.email
        data = json.dumps(addUserData)
        print(data)

        response = requests.put(TestPersonalData.baseUrlCustomers + TestPersonalData.email,
                                data=json.dumps(data),
                                headers=TestPersonalData.headers)
        print(response)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

    def insert_or_update_personal_data(self):
        response = requests.put(TestPersonalData.baseUrlCustomers + 'current@example.com',
                                data=json.dumps(TestPersonalData.data['addNewUser']), headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

    def add_and_delete_profile(self):
        response = requests.put(TestPersonalData.baseUrlCustomers + 'current@example.com',
                                data=json.dumps(TestPersonalData.data['userForDel']), headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

        respD = requests.delete(TestPersonalData.baseUrlCustomers + 'testadduser11@example.com',
                                data=json.dumps(TestPersonalData.data['forDelete']), headers=TestPersonalData.headers)

        data_json = json.loads(respD.text)
        assert data_json['type'] == 1
        assert respD.status_code == 200

    def getting_information_by_email(self):
        response = requests.get(TestPersonalData.baseUrlCustomers + 'new11@example.com')
        data_json = json.loads(response.text)
        assert data_json['type'] == 1
        assert response.status_code == 200

    def getting_statistics_on_personal_data(self):
        response = requests.get(TestPersonalData.baseUrl +"stats")
        data_json = json.loads(response.text)
        assert data_json['type'] == 1
        assert response.status_code == 200
