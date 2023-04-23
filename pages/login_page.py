import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    scouts_panel_title_xpath = "//div[@class='MuiCardContent-root']//h5"
    listbox_language_xpath = "//div[@aria-haspopup='listbox']"
    remaind_password_hyperlink_xpath = "//a [text()='Remind password']"
    # TASK3 - Subtask 3: Assert
    expected_title = "Scouts panel - sign in" # TASK3 - Subtask 2: Nowy przypadek testowy
    login_url = "https://scouts-test.futbolkolektyw.pl/login" # TASK3 - Subtask 2: Nowy przypadek testowy

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    #TASK3 - Subtask 1: Uzupełnienie strony logowania
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    # TASK3 - Subtask 3: Assert
    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.login_url) == self.expected_title

    #def get_page_title(self, login_url):
        #pass