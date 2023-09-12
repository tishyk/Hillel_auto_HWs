# Написати тести на створювання користувача, та логін у систему.
#
# Тест на перевірку профіля користувача
#
# Написати параметризований тест, на перевірку реєстрації з правильними та неправильними паролями

import requests
import pytest
class UserSignUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password




user_sign_up = UserSignUpModel("John", "Dou", "test_rubachek14@test.com", "Qwerty12345", "Qwerty12345")
user_sign_up_error = UserSignUpModel("John", "Dou", "test_rubachek15@test.com", "qwerty12345", "werty12345")

sessions = requests.session()



def test_post_new_user():
    post_new_user = sessions.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_sign_up.__dict__)
    assert post_new_user.status_code == 201
def test_get_current_user():
    get_current_user = sessions.get("https://qauto2.forstudy.space/api/users/current")
    assert get_current_user.status_code == 200

def test_delete_user():
    test_delete_user = sessions.delete('https://qauto2.forstudy.space/api/users')
    assert test_delete_user.status_code == 200
def test_post_new_user_error():
    post_new_user = sessions.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_sign_up_error.__dict__)
    assert post_new_user.status_code == 400


# Или вариант через параметры

# Написати параметризований тест, на перевірку реєстрації з правильними та неправильними паролями
# не понимаю как сделать парамертизированый запрос на Get в документации которого ни слова о параметрах. Сделал запрос тет на вход https://qauto2.forstudy.space/api/users/profile

# @pytest.mark.parametrize(("email", "password"), [("test_rubachek1@test.com", "Qwerty12345"), ("test_rubachek1@test.com", "werty12345")])
# def test_post_current_profile(email, password):
#     user_sign_up_parametrize = {"email": email, "password": password}
#     post_current_user_profile = requests.post("https://qauto2.forstudy.space/api/auth/signin", json=user_sign_up_parametrize)
#     assert (post_current_user_profile.status_code == 200

@pytest.mark.parametrize(("email", "password"), [("test_rubachek1@test.com", "Qwerty12345"), ("test_rubachek1@test.com", "werty12345")]))
def test_post_current_profile(email, password):
    user_sign_up_parametrize = {"email": email, "password": password}
    post_current_user_profile = requests.get("https://qauto2.forstudy.space/api/auth/signin", headers=user_sign_up_parametrize)
    assert post_current_user_profile.status_code == 200


#параметоризированный на создание
# @pytest.mark.parametrize("name,last_name,email,password,repeat_password", [
#     ("John", "Dou", "test_rubachek16@test.com", "Qwerty12345", "Qwerty12345"),
#     ("John", "Dou", "test_rubachek17@test.com", "qwerty12345", "werty12345")
# ])
# def test_post_new_user_parametrize(name, last_name, email, password, repeat_password):
#     user_sign_up_parametrize = UserSignUpModel(name, last_name, email, password, repeat_password)
#     post_new_user_parametrize = sessions.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_sign_up_parametrize.__dict__)
#     assert post_new_user_parametrize.status_code == 201 or post_new_user_parametrize.status_code == 400
