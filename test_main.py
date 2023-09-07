import requests

class UserSignUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password




user_sign_up = UserSignUpModel("John", "Dou", "test_rubachek5@test.com", "Qwerty12345", "Qwerty12345")


# text_dic = {
#   "name": "John",
#   "lastName": "Dou",
#   "email": "test_rubachek3@test.com",
#   "password": "Qwerty12345",
#   "repeatPassword": "Qwerty12345"
# }

sessions = requests.session()

get_current_user = sessions.get("https://qauto2.forstudy.space/api/users/current")
post_new_user = sessions.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_sign_up.__dict__)
get_current_user_after_post = sessions.get("https://qauto2.forstudy.space/api/users/current")
print(get_current_user.text)
print(post_new_user.text)
print(get_current_user_after_post.text)





# import pytest


#
#
# @pytest.mark.parametrize("furst_num,second_num,expected_sum", [(1, 2, 3), (5, 5, 11), (2, 2, 4)])
# def test_check_sum(furst_num, second_num, expected_sum ):
#     assert custom_sum(furst_num, second_num) == expected_sum
#
#
# def custom_sum(furst_num, second_num):
#     return furst_num + second_num