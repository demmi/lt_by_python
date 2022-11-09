# Lesson 08 API testing

import requests  # это модуль Python для отправки всех видов HTTP-запросов
import pytest
import time

base_url = 'https://jsonplaceholder.typicode.com/'  # это ресурс
HTTP_code = 200  # задаем статус


@pytest.mark.skip
def test_get_all_posts():  # метод get для получения данных
    response = requests.get(f'{base_url}posts')  # получить все посты с https://jsonplaceholder.typicode.com/posts
    assert response.status_code == HTTP_code, 'wrong status code'  # проверить код ответа
    # print(response.json())  # для контроля запустим: pytest -s -v test_api_08.py
    # PASSED, распечатались все сто постов, лучше запросим их количество:
    # print(len(response.json()))  # test_api_08.py::test_get_all_posts 100 PASSED.
    # Сделаем из этого проверку:
    assert len(response.json()) == 100, 'actual length does not match to expected'
    # test_api_08.py::test_get_all_posts PASSED


@pytest.mark.skip
def test_get_post1():
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


# ----- Параметризация -----

# Напишем функцию для получения списка всех пользователей:
def get_all_names():
    response = requests.get(f'{base_url}users/')
    response_data = response.json()
    name_list = []
    for i, name in enumerate(response_data):  # enumerate вернет кортеж с номером элемента и его значением
        name_list.append((i + 1, response_data[i]['name']))
    return name_list

# Напишем тест, который будет запускаться отдельно для каждого параметра (для каждого из 10 пользователей)


@pytest.mark.skip
@pytest.mark.parametrize('userid, expected_name', get_all_names())
def test_get_all_users_name(userid, expected_name):
    response = requests.get(f'{base_url}users/{userid}')  # endpoint is userid
    response_data = response.json()
    assert response_data['name'] == expected_name, 'wrong name'

# Тест проверил все имена. Результат:
# test_api_08.py::test_get_all_users_name[1-Leanne Graham] PASSED
# test_api_08.py::test_get_all_users_name[2-Ervin Howell] PASSED
# test_api_08.py::test_get_all_users_name[3-Clementine Bauch] PASSED
# test_api_08.py::test_get_all_users_name[4-Patricia Lebsack] PASSED
# test_api_08.py::test_get_all_users_name[5-Chelsey Dietrich] PASSED
# test_api_08.py::test_get_all_users_name[6-Mrs. Dennis Schulist] PASSED
# test_api_08.py::test_get_all_users_name[7-Kurtis Weissnat] PASSED
# test_api_08.py::test_get_all_users_name[8-Nicholas Runolfsdottir V] PASSED
# test_api_08.py::test_get_all_users_name[9-Glenna Reichert] PASSED
# test_api_08.py::test_get_all_users_name[10-Clementina DuBuque] PASSED


url = 'https://playground.learnqa.ru/api/'  # Возьмем другой сайт


def test_end_to_end():
    new_user = {
        'username': 'my user',
        'firstName': 'MyFirstname',
        'lastName': 'MyLastname',
        'email': str(time.time()) + '@example.com',
        'password': '12345'
    }

# Создадим нового пользователя
    response = requests.post(f'{url}user', data=new_user)  # endpoint is user, передаем данные new_user
    assert response.status_code == 200

# Проверим, что создали
    response_data = response.json()
    assert 'id' in response_data.keys()  # проверяем, что id есть в ключах response_data.keys()

    user_id = response_data['id']
    response = requests.get(f'{url}user/{user_id}')  # запрос на получение данных по user_id
    assert response.status_code == 200
    # print(response.json())  # test_api_08.py::test_end_to_end {'username': 'my user'}
    # print('get==>', response.headers)

# Авторизуем нового пользователя
    auth_data = {  # создаем словарь с данными нового пользователя, чтобы пройти авторизацию
        'email': new_user['email'],
        'password': '12345'
    }

    response = requests.post(f'{url}user/login', data=auth_data)  # запрос на авторизацию с данными auth_data
    assert response.status_code == HTTP_code, 'wrong status code'  # если авторизация успешна, д.б. статус 200
# ///// 1:20:26
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
# ///// 14:26
