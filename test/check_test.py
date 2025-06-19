import requests

# Создать задачу. Проставить отметку о выполнении и проверить что completed ==True
def test_add():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://sky-todo-list.herokuapp.com/", json=body)
    body1 = {"title": "generated", "completed": True}
    response_check = requests.patch("https://sky-todo-list.herokuapp.com/", json=body1)

    assert response.status_code == 200
    assert response_check['completed'] == True

