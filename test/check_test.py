import requests

# Создать задачу. Проставить отметку о выполнении и проверить что completed ==True
def test_add():
    body = {"title": "generated", "completed": True}
    response = requests.post("https://sky-todo-list.herokuapp.com/", json=body)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['completed'] == True

