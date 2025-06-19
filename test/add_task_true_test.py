import requests


def test_add_true():
    body = {"title": "generated", "completed": True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    print(response.status_code)
    print(response_body)

    assert response.status_code == 200
    assert response_body['completed'] is True
