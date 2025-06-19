import requests


def test_add_new():
    import requests

    def test_add():
        body = {"title": "generated", "completed": False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
        response_body = response.json()

        assert response.status_code == 202
        assert response_body['completed'] == False

    def test_create_and_delete():
        create_body = {"title": "For delete", "completed": False}
        create_response = requests.post("https://todo-app-sky.herokuapp.com/", json=create_body)
        create_response_body = create_response.json()

        assert create_response.status_code == 202
        assert create_response_body['completed'] == False

        task_id = create_response_body['id']

        delete_response = requests.delete(f"https://todo-app-sky.herokuapp.com/{task_id}")

        assert delete_response.status_code == 204

        get_response = requests.get(f"https://todo-app-sky.herokuapp.com/{task_id}")

        assert get_response.status_code == 404
