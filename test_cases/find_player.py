import os
import time
import unittest

from selenium import webdriver

from pages.add_a_player_form import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.players_page import PlayersPage
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestFindPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_find_player(self):
        TestLoginPage.test_log_in_to_the_system(self)

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_players_button()open_

        players_page = PlayersPage(self.driver)
        players_page.click_filter_button()
        players_page.type_in_name_field('TestName')
        players_page.type_in_surname_field('TestSurname')
        players_page.type_in_main_position_field('TestMainPosition')
        players_page.click_close_filter_button()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()