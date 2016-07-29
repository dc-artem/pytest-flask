from flask import Flask
from flask import Response, json
from flask.testing import FlaskClient




app = Flask(__name__)

def test_app(client):
    response = client.get('http://personal-data-service.dev' + 'stats/')
    assert response.status_code == 200
    assert isinstance(response, Response)

    json_data = json.loads(response.data.decode('utf-8'))
    print(json_data)
    assert isinstance(json_data, list)
    print(json_data)
    # assert response.json['type'] == '1'