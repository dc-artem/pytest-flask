import requests
import json
import os.path
from test_API.mail_random_generator import generate_random_email


class TestPersonalData:

    email = generate_random_email(7)
    emailfordeluser = generate_random_email(7)

    config = "target.json"
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), config)
    # with open('target.json', 'r', encoding='utf-8') as fh:
    with open(config_file) as fh:
        data = json.load(fh)
    headers = {
        'Content-type': 'application/json'
    }
    baseUrlCustomers = data['urls']["baseUrlCustomers"]
    baseUrl = data['urls']["baseUrl"]

    def request_information_about_system(self):
        pass

    def test_insert_personal_data(self):
        addUserData = TestPersonalData.data['addNewUser']
        addUserData['customerInfo']['email'] = TestPersonalData.email
        data = json.dumps(addUserData)
        response = requests.put(TestPersonalData.baseUrlCustomers + TestPersonalData.email,
                                data=json.dumps(data),
                                headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

    def test_insert_and_update_personal_data(self):
        """
        Добавлем нового пользователя с емейлом current@example.com
        """
        response = requests.put(TestPersonalData.baseUrlCustomers + 'current@example.com',
                                data=json.dumps(TestPersonalData.data['addUser']),
                                headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

        """
        Обновляем данные для пользователя с емейлом current@examle.com

        """
        response = requests.put(TestPersonalData.baseUrlCustomers + 'current@example.com',
                                data=json.dumps(TestPersonalData.data['editPersonalDate']),
                                headers=TestPersonalData.headers)
        data_json2 = json.loads(response.text)

        assert data_json2['type'] == 1
        assert response.status_code == 200

    def test_add_and_delete_profile(self):
        """
        Добавление нового пользователя с уникальным емейлом
        """

        addUserData = TestPersonalData.data['userForDel']
        addUserData['customerInfo']['email'] = TestPersonalData.emailfordeluser
        data = json.dumps(addUserData)

        response = requests.put(TestPersonalData.baseUrlCustomers + TestPersonalData.emailfordeluser,
                                data=json.dumps(data),
                                headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

        """
        Удаление пользователя с уникальным емейлом
        """
        delUserData = TestPersonalData.data['forDelete']
        delUserData['deletion']['initiator'] = TestPersonalData.emailfordeluser
        datadel = json.dumps(delUserData)

        respD = requests.delete(TestPersonalData.baseUrlCustomers + TestPersonalData.emailfordeluser,
                                data=datadel, headers=TestPersonalData.headers)

        data_json = json.loads(respD.text)

        assert respD.status_code == 200
        assert data_json['type'] == 1


    def test_getting_information_by_email(self):
        response = requests.get(TestPersonalData.baseUrlCustomers + TestPersonalData.email)
        data_json = json.loads(response.text)
        assert data_json['type'] == 1
        assert response.status_code == 200

    def test_getting_statistics_on_personal_data(self):
        response = requests.get(TestPersonalData.baseUrl + "stats")
        data_json = json.loads(response.text)
        assert data_json['type'] == 1
        assert response.status_code == 200
