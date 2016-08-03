import requests
import json
import os.path
from test_api.mail_random_generator import generate_random_email
from test_api.incorrect_mail_random_generator import generate_random_incorrect_email


class TestPersonalData:

    email = generate_random_email(7)
    emailForDelUser = generate_random_email(7)
    incorrectEmail = generate_random_incorrect_email(7)

    config = "target.json"
    config_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), config)
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
        addUserData['customerInfo']['email'] = TestPersonalData.emailForDelUser
        data = json.dumps(addUserData)

        response = requests.put(TestPersonalData.baseUrlCustomers + TestPersonalData.emailForDelUser,
                                data=json.dumps(data),
                                headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 1
        assert response.status_code == 200

        """
        Удаление пользователя с уникальным емейлом
        """
        delUserData = TestPersonalData.data['forDelete']
        delUserData['deletion']['initiator'] = TestPersonalData.emailForDelUser
        datadel = json.dumps(delUserData)

        respD = requests.delete(TestPersonalData.baseUrlCustomers + TestPersonalData.emailForDelUser,
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


# Scenario Outline: negative_get_customers_INFO_by_email
# #  Получение данных о пользователе по некорректному email
#   Given I have incorrect email
#   When I send request customer incorrect email INFO - [GET]
# #  http://personal-data-service.dev/customers/ksdjhfksd
#   Then I get status 400 and type 3
# #email:\n    This value is not a valid email address. (code bd79c0ab-ddba-46cc-a703-a7a4b08de310)\n",


    def test_negative_get_customers_INFO_by_email(self):
        response = requests.get(TestPersonalData.baseUrlCustomers + TestPersonalData.incorrectEmail)
        data_json = json.loads(response.text)
        assert data_json['type'] == 3
        assert response.status_code == 400

#
# Scenario: negative_UPSERT_put_add_user_which_has_been_deleted
#   Попытка добавить пользователя, - который ранее был удалён
#   Given I delete user [DEL]
# #  http://personal-data-service.dev/customers/bla@bla.ru
#   When I try add this user again [PUT]
# #  http://personal-data-service.dev/customers/bla@bla.ru
#   Then I get status 400 and type 3
# # "error": "Business rule checking failed"

    # def test_negative_UPSERT_put_add_user_which_has_been_deleted(self):
    #     # этот метод уже был использован ранее. он должен заускатся
    #     test_add_and_delete_profile()
    #
    #     #Далее запускается код, который отправляет повторно данные из метода выше.
    #     response = requests.put(TestPersonalData.baseUrlCustomers + TestPersonalData.emailForDelUser,
    #                             data=json.dumps(data),
    #                             headers=TestPersonalData.headers)
    #     data_json = json.loads(response.text)
    #
    #     assert data_json['type'] == 4
    #     assert response.status_code == 400
    #
# Scenario: negativ_DEL_delete_with_incorrect_email
#   Given I have incorrect email
#   When I send request customer incorrect email DELETE - [DELETE]
# #  http://personal-data-service.dev/customers/emailjdshgf
#   Then I get status 400 and type 3
# #  This value is not a valid email address. (code bd79c0ab-ddba-46cc-a703-a7a4b08de310)\n",


    def test_negative_DEL_delete_with_incorrect_email(self):
        delUserData = TestPersonalData.data['forDelete']
        delUserData['deletion']['initiator'] = TestPersonalData.incorrectEmail
        datadel = json.dumps(delUserData)

        respD = requests.delete(TestPersonalData.baseUrlCustomers + TestPersonalData.incorrectEmail,
                                data=datadel, headers=TestPersonalData.headers)
        data_json = json.loads(respD.text)

        assert respD.status_code == 400
        assert data_json['type'] == 3


# Scenario: negativ_UPSERT_add_user_incorrect-email
# #  Попытка добавить пользователя с некорректным email
#   Given I have incorrect email
#   When I send request customer incorrect email UPSERT - [PUT]
# #  http://personal-data-service.dev/customers/kjdssf
#   Then I get status 400 and type 3
# #  "error": This value is not a valid email address. (code bd79c0ab-ddba-46cc-a703-a7a4b08de310)\nObjec

    def test_negativ_UPSERT_add_user_incorrect_email(self):
        addUserData = TestPersonalData.data['addNewUser']
        addUserData['customerInfo']['email'] = TestPersonalData.incorrectEmail
        data = json.dumps(addUserData)
        response = requests.put(TestPersonalData.baseUrlCustomers + TestPersonalData.incorrectEmail,
                                data=json.dumps(data),
                                headers=TestPersonalData.headers)
        data_json = json.loads(response.text)

        assert data_json['type'] == 3
        assert response.status_code == 400