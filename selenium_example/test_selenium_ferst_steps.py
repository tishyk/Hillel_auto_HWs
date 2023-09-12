from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pytest


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")

# registration
class TestRegisteration:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.session = requests.session()

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def test_registration(self):
        sign_up_button = self.driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        name_field = self.driver.find_element(By.ID, "signupName")
        name_field.send_keys("nametest")
        last_name_field = self.driver.find_element(By.ID, "signupLastName")
        last_name_field.send_keys("lastnametest")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        email_field.send_keys("test_rubachek36@test.com")
        password_field = self.driver.find_element(By.ID, "signupPassword")
        password_field.send_keys("Qwerty123")
        repeat_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_field.send_keys("Qwerty123")
        register_button = self.driver.find_element(By.XPATH, '//button[text()="Register"]')
        register_button.click()
        p_text_after_registration = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//p[text()="You don’t have any cars in your garage"]'))
        )
        # self.session.delete("https://qauto2.forstudy.space/api/users")
        assert len(p_text_after_registration.text) == 38
    def test_delete_user(self): # все что ниже из за того что def teardown_method(self) не работает
        self.driver.get("https://qauto2.forstudy.space/panel/settings")
        delete_users = self.driver.find_element(By.XPATH, "//button[text()='Remove my account']")
        delete_users.click()
        delete_users_confirm = self.driver.find_element(By.XPATH, "//button[text()='Remove']")
        delete_users_confirm.click()  # как проверить что удаление прошло успешно если это конец теста?

    # не знаю как заставить его работать
    # def teardown_class(self):
    #     self.session.delete("https://qauto2.forstudy.space/api/users")


