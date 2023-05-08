import os
import unittest
import time
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player_form import AddAPlayer


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(3)
        dashboard_page.click_english_button()
        time.sleep(3)
        dashboard_page.click_add_a_player_button()
        time.sleep(3)
        add_a_player = AddAPlayer(self.driver)
        add_a_player.title_of_page()
        time.sleep(3)
        add_a_player.type_in_name('Marian')
        add_a_player.type_in_surname('Nowak')
        add_a_player.type_in_age('10.08.1987')
        add_a_player.type_in_main_position('goalkeeper')
        add_a_player.click_submit_button()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()