from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pytest

from selenium_example.facade.registration_facade import RegistrationFacade
from selenium_example.pages.garege_page import GaragePage
from selenium_example.pages.main_page import MainPage
from selenium_example.pages.registration_form_page import RegistrationFormPage


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")

# registration

class TestDase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.Session()
        self._registration_facade = RegistrationFacade(self._driver)


        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


    def teardown_method(self):
        self._driver.close()


class TestRegisteration(TestDase):

    def setup_class(self):
        # self.driver.implicitly_wait(3)
        # self.session = requests.Session()
        self.user_email = "test_rubachek46@test.com"
        self.user_password = "Qwerty12345"
        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }



    def teardown_method(self):
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_to_login)
        self._session.delete(url="https://qauto2.forstudy.space/api/users")

    def test_registration(self):
        self._registration_facade.registration_user("test", 'testlastname', self.user_email, self.user_password, self.user_password)
        assert self._registration_facade.check_is_user_logged_in()

    # def test_delete_user(self): # все что ниже из за того что def teardown_method(self) не работает
    #     self.driver.get("https://qauto2.forstudy.space/panel/settings")
    #     delete_users = self.driver.find_element(By.XPATH, "//button[text()='Remove my account']")
    #     delete_users.click()
    #     delete_users_confirm = self.driver.find_element(By.XPATH, "//button[text()='Remove']")
    #     delete_users_confirm.click()  # как проверить что удаление прошло успешно если это конец теста?
