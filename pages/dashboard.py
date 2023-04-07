from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_title_xpath = "//header/div/h6"
    main_page_button_xpath = "//span[text()='Main page']//ancestor-or-self::div[@role='button']"
    players_button_xpath = "//ul[1]/div[2]"
    change_language_button_xpath = "//*/ul[2]/div[1]"
    sign_out_button_xpath = "//span[text()='Sign out']//ancestor-or-self::div[@role='button']"
    add_player_button_xpath = "//*[2][name() = 'a']/button"
    dev_team_contact_button_xpath = "//a[@target='_blank']"
    logo_scouts_panel_xpath = "//div[@title='Logo Scouts Panel']"
    players_count_section_xpath = "//div[text()='Players count']/parent::div/parent::div"
    matches_count_section_xpath = "// div[text() = 'Matches count'] / parent::div / parent::div"
    reports_count_section_xpath = "//div[text()='Reports count']/parent::div/parent::div"
    pass
