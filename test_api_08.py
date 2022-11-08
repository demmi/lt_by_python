# Lesson 08 API testing

import requests  # это модуль Python для отправки всех видов HTTP-запросов
import pytest
import time

base_url = 'https://jsonplaceholder.typicode.com/'  # это ресурс
HTTP_code = 200  # задаем статус
# url = 'https://playground.learnqa.ru/api/'


@pytest.mark.skip
def test_get_all_posts():
    response = requests.get(f'{base_url}posts')  # получить все посты с https://jsonplaceholder.typicode.com/posts
    assert response.status_code == HTTP_code, 'wrong status code'  # проверить код ответа
    # print(response.json())  # для контроля запустим: pytest -s -v test_api_08.py
    # PASSED, распечатались все сто постов, лучше запросим их количество:
    # print(len(response.json()))  # test_api_08.py::test_get_all_posts 100 PASSED.
    # Сделаем из этого проверку:
    assert len(response.json()) == 100, 'actual length does not match to expected'
    # test_api_08.py::test_get_all_posts PASSED


@pytest.mark.skip
def test_get_post1():  # метод get для получения данных
    response = requests.get(f'{base_url}posts/1')  # получить 1-й пост с base_url
    assert response.status_code == HTTP_code, 'wrong status code'
    response_data = response.json()  # отклик в формате json зададим в виде переменной response_data
    # посмотрим, что в этом файле хранится:
    # print(response_data)  # выведен словарь с данными пользователя: {'userId': 1, 'id': 1, ... всего 4 элемента}
    expected_keys = ['userId', 'id', 'title', 'body']  # допустим, надо проверить наличие этих ключей
    for key in response_data.keys():  # для каждого ключа из ключей .keys(), полученных в отклике response_data
        assert key in expected_keys, 'wrong keys'  # проверим, что этот ключ есть в списке expected_keys


@pytest.mark.skip
def test_post_in_posts():  # метод post для отправки данных, которые создадим в post_data
    post_data = {
        'id': 101,
        'title': 'my title',
        'body': 'my body'
    }
    response = requests.post(f'{base_url}posts', data=post_data)  # отправить post_data в endpoint posts
    assert response.status_code == 201, 'wrong code'  # для метода post успешный ответ сервера - код 201
    response_data = response.json()
    expected_title = 'my title'  # ожидаемая запись для ключа 'title'
    assert response_data['title'] == expected_title

# ///// 45:33
# def get_all_names():
#     response = requests.get(f'{base_url}users/')
#     response_data = response.json()
#     name_list = []
#     for i, name in enumerate(response_data):
#         name_list.append((i + 1, response_data[i]['name']))
#     return name_list
#
#
# @pytest.mark.skip
# @pytest.mark.parametrize('userid, expected_name', get_all_names())
# def test_get_all_users_name(userid, expected_name):
#     response = requests.get(f'{base_url}users/{userid}')
#     response_data = response.json()
#     assert response_data['name'] == expected_name, 'wrong name'
#
#
# def test_end_to_end():
#     new_user = {
#         'username': 'my user',
#         'firstName': 'MyFirstname',
#         'lastName': 'MyLastname',
#         'email': str(time.time()) + '@example.com',
#         'password': '12345'
#     }
#
#     response = requests.post(f'{url}user', data=new_user)
#     assert response.status_code == 200
#
#     response_data = response.json()
#     assert 'id' in response_data.keys()
#     user_id = response_data['id']
#
#     response = requests.get(f'{url}user/{user_id}')
#     assert response.status_code == 200
#     print('get==>', response.headers)
#
#     auth_data = {
#         'email': new_user['email'],
#         'password': '12345'
#     }
#
#     response = requests.post(f'{url}user/login', data=auth_data)
#     assert response.status_code == HTTP_code, 'wrong status code'
#     token = response.headers['x-csrf-token']
#     auth_sid = response.cookies['auth_sid']
#
#     new_user_update = {
#         'username': 'my user updated'
#     }
#
#     response = requests.put(f'{url}user/{user_id}',
#                             data=new_user_update,
#                             headers={'x-csrf-token': token},
#                             cookies={'auth_sid': auth_sid})
#
#     assert response.status_code == 200, 'wrong status code'
#
#     response = requests.get(f'{url}user/{user_id}')
#     assert response.status_code == HTTP_code
#
#     response_data = response.json()
#     assert 'my user updated' in response_data.values()
#     print('response_data==>', response_data)
#
#     response = requests.delete(f'{url}user/{user_id}',
#                                headers={'x-csrf-token': token},
#                                cookies={'auth_sid': auth_sid})
#
#     response = requests.get(f'{url}user/{user_id}')
#     assert response.status_code == 404
#
#
# # ///// 14:26
