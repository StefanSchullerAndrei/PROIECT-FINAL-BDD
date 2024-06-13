from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    Login_Page_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    Username_Input = (By.CSS_SELECTOR, "input[name='username']")
    Password_Input = (By.XPATH, "//input[@name='password']")
    Login_button = (By.CSS_SELECTOR, "button[type='submit']")
    Error_Displayed = (By.CSS_SELECTOR, "div[role='alert']")
    Error_Message = (By.CSS_SELECTOR, "p.oxd-alert-content-text")
    DASHBOARD_PAGE = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Search']")


    def navigate_to_login_page(self):
        self.driver.get(self.Login_Page_URL)

    def incorrect_username(self, username):
        self.type(self.Username_Input, username)

    def correct_password(self, password):
        self.type(self.Password_Input, password)

    def click_login_button(self):
        self.click(self.Login_button)

    def error_displayed(self):
        self.is_displayed(self.Error_Displayed)

    def error_message(self, message):
        assert message in self.get_text(self.Error_Message)

    def correct_username(self, username):
        self.type(self.Username_Input, username)

    def incorrect_password(self, password):
        self.type(self.Password_Input, password)

    def redirect_to_the_dashboard_page(self):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        assert self.driver.current_url == expected_url





