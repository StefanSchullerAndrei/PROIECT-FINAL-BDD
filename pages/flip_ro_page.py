import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random


class LoginPage_Flip(BasePage):
    LOGIN_PAGE_URL = "https://flip.ro/magazin/"
    CONTUL_MEU_BUTTON = (By.XPATH, "//span[normalize-space()='Contul meu']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='login-email']")
    PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_BUTTON = (By.XPATH, "//span[normalize-space()='Acceseaza cont']")
    ERROR_LOGIN_MESSAGE = (By.XPATH, "//div[@class='toasted bubble error']")
    ACCEPT_COOKIE = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/button[1]/span")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def accept_cookies(self):
        self.click(self.ACCEPT_COOKIE)

    def click_contul_meu(self):
        self.click(self.CONTUL_MEU_BUTTON)

    def input_random_email(self):
        random_number = random.randint(1, 9999999999999)
        address_email = f'andrei_st{random_number}@gm.ro'
        self.type(self.EMAIL_INPUT, address_email)
        time.sleep(2)

    def input_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def email_message_displayed(self, expected_error_message):
        try:
            error_message_text = self.driver.find_element(*self.ERROR_LOGIN_MESSAGE).text.replace("ș", "s").replace("ă",
                                                                                                                    "a")
        except:
            pass
        assert self.is_displayed(self.ERROR_LOGIN_MESSAGE) == True

        assert expected_error_message == error_message_text, f"Expected message {expected_error_message}, actual error message {error_message_text}"

    def error_message(self, expected_error):
        try:
            error_message_text = self.driver.find_element(*self.ERROR_LOGIN_MESSAGE).text.replace("ș", "s")
        except:
            pass
        assert self.is_displayed(self.ERROR_LOGIN_MESSAGE) == True

        assert expected_error == error_message_text, f"Expected message {expected_error}, actual error message {error_message_text}"

    def input_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def input_password_1(self, password1):
        self.type(self.PASSWORD_INPUT, password1)


