import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class SignUp_Page(BasePage):
    JULES_URL = "https://jules.app/sign-in"
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "a[class='jss17 jss19']")
    PERSONAL_BUTTON = (By.CSS_SELECTOR, "input[value='personal']")
    CONTINUE_BUTTON = (By.XPATH, "//span[normalize-space()='CONTINUE']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[placeholder='Type your answer here...']")
    LAST_NAME = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div/div[2]/div/div/input")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Type your answer here...']")
    ERROR_MESSAGE = (By.XPATH, "//div[@id='root']//p")

    def navigate_to_sign_up(self):
        self.driver.get(self.JULES_URL)

    def click_sign_up_button(self):
        self.click(self.SIGN_UP_BUTTON)

    def click_option(self):
        self.click(self.PERSONAL_BUTTON)
        time.sleep(3)

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def set_first_name(self, firstname):
        self.type(self.FIRST_NAME, firstname)

    def set_last_name(self, lastname):
        self.type(self.LAST_NAME, lastname)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def verify_message_displayed(self, expected_error_message):
        # actual_message = self.get_text(self.ERROR_MESSAGE)
        # print(f"Verifying message: {verifymessage} in {actual_message}")
        # assert verifymessage in actual_message
        actual_error = self.driver.find_element(*self.ERROR_MESSAGE).text
        assert expected_error_message == actual_error, f"Error: Invalid message. expected: {expected_error_message}, actual: {actual_error}"