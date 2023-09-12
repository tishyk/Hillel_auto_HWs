import requests
import pytest

class UserSignUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password







class TestRegisteration:
    def setup_class(self):
        self.user_sign_up = UserSignUpModel("John", "Dou", "test_rubachek56@test.com", "Qwerty12345", "Qwerty12345")
    def setup_method(self):
        self.session = requests.session()
    def test_chek_successful_registration(self):
        post_new_user = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_sign_up.__dict__)
        assert post_new_user.status_code == 201

    def test_chek_successful_registration1(self):
        post_new_user = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_sign_up.__dict__)
        assert post_new_user.status_code == 201

    def teardown_method(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")



#
# import pytest




# @pytest.mark.parametrize("furst_num,second_num,expected_sum", [(1, 2, 3), (5, 5, 11), (2, 2, 4)])
# def test_check_sum(furst_num, second_num, expected_sum ):
#     assert custom_sum(furst_num, second_num) == expected_sum
#
#
# def custom_sum(furst_num, second_num):
#     return furst_num + second_num

