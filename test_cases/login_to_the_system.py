import os
import unittest
import time
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard

# TASK3 - Subtask 2: Nowy przypadek testowy
class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page() # TASK3 - Subtask 3: Assert
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        time.sleep(5)
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver) # TASK3 - Subtask 3: Assert
        dashboard_page.title_of_page() # TASK3 - Subtask 3: Assert
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()