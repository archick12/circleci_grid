import pytest
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


class TestJiraLoginUI:

    @pytest.mark.test_case(parameters={"id": "1"})
    @pytest.mark.smoke
    def test_login_to_jira(self, browser):
        self.login_page = LoginPage(browser)
        self.login_page.open("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        assert self.login_page.at_page()
        self.login_page.login_to_jira_enter_username("webinar5")
        self.login_page.login_to_jira_enter_password("webinar5")
        self.login_page.click_login_button_at_main_page()
        self.main_page = MainPage(browser)
        self.main_page.is_assigned_to_me_section()
        assert self.main_page.is_assigned_to_me_section()

    @pytest.mark.test_case(parameters={"id": "2"})
    def test_passed_test(self):
        assert 1 !=1

