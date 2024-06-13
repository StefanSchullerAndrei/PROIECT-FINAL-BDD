from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ParabankRegister_Page(BasePage):
    PARABANK_HOME_LINK = "https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC"
    REGISTER_BUTTON = (By.LINK_TEXT, "Register")
    FIRST_NAME_FIELD = (By.ID, 'customer.firstName')
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'customer.lastName')
    LAST_NAME = (By.ID, "lastName")
    ADDRESS_FIELD = (By.ID, 'customer.address.street')
    ADDRESS_FIELD_LOGIN_INFO = (By.ID, "address.street")
    CITY_FIELD = (By.ID, 'customer.address.city')
    CITY_FIELD_LOGIN_INFO = (By.ID, "address.city")
    STATE_FIELD = (By.ID, 'customer.address.state')
    STATE_FIELD_LOGIN_INFO = (By.ID, "address.state")
    ZIPCODE_FIELD = (By.ID, 'customer.address.zipCode')
    ZIPCODE_FIELD_LOGIN_INFO = (By.ID, "address.zipCode")
    PHONE_NUMBER_FIELD = (By.ID, 'customer.phoneNumber')
    SSN_FIELD = (By.ID, 'customer.ssn')
    SSN_FIELD_LOGIN_INFO = (By.ID, "ssn")
    USERNAME_FIELD = (By.ID, 'customer.username')
    PASSWORD_FIELD = (By.ID, 'customer.password')
    CONFIRM_PASSWORD_FIELD = (By.ID, 'repeatedPassword')
    REGISTER_BUTTON_CONFIRM = (By.CSS_SELECTOR, 'input[value="Register"]')
    SSN_ERROR = (By.ID, 'customer.ssn.errors')
    LOG_OUT_BUTTON = (By.XPATH, "//a[normalize-space()='Log Out']")
    FORGOT_LOGIN_INFO_BUTTON = (By.XPATH, "//a[normalize-space()='Forgot login info?']")
    FIND_MY_LOGIN_INFO_BUTTON = (By.XPATH, "//input[@value='Find My Login Info']")
    USERNAME_FOUND = (By.XPATH, "//b[normalize-space()='Username']")
    PASSWORD_FOUND = (By.XPATH, "//b[normalize-space()='Password']")


    def navigate_to_page(self):
        self.driver.get(self.PARABANK_HOME_LINK)

    def click_register_button(self):
        self.click(self.REGISTER_BUTTON)

    def insert_firstname(self, firstname):
        self.type(self.FIRST_NAME_FIELD, firstname)

    def insert_lastname(self, lastname):
        self.type(self.LAST_NAME_FIELD, lastname)

    def insert_address(self, address):
        self.type(self.ADDRESS_FIELD, address)

    def insert_city(self, city):
        self.type(self.CITY_FIELD, city)

    def insert_state(self, state):
        self.type(self.STATE_FIELD, state)

    def insert_zipcode(self, zipcode):
        self.type(self.ZIPCODE_FIELD, zipcode)

    def insert_phonenumber(self, phonenumber):
        self.type(self.PHONE_NUMBER_FIELD, phonenumber)

    def insert_ssn(self, ssn):
        self.type(self.SSN_FIELD, ssn)

    def insert_username(self, username):
        self.type(self.USERNAME_FIELD, username)

    def insert_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def insert_confirm_password(self, password):
        self.type(self.CONFIRM_PASSWORD_FIELD, password)

    def click_register(self):
        self.click(self.REGISTER_BUTTON_CONFIRM)

    def error_register_credentials(self):
        # error_message = self.get_text(self.SSN_ERROR)

        current_url = self.driver.current_url
        expected_url = 'https://parabank.parasoft.com/parabank/register.htm'
        # if current_url == error_message:
        #     print(f': {current_url}')

        if current_url == expected_url:
            print(f'The register process is not perfect. "Your account was created successfully. You are now logged in." was displayed on the next page: {current_url}')

    def click_logout_button(self):
        wait = WebDriverWait(self.driver, 10)  # Așteaptă până la 10 secunde
        logout_button = wait.until(EC.element_to_be_clickable(self.LOG_OUT_BUTTON))
        logout_button.click()

    def click_forgot_login_info_button(self):
        self.click(self.FORGOT_LOGIN_INFO_BUTTON)

    def click_find_my_login_info_button(self):
        self.click(self.FIND_MY_LOGIN_INFO_BUTTON)

    def insert_firstname_login(self, firstname_login):
        self.type(self.FIRST_NAME, firstname_login)

    def insert_lastname_login(self, lastname_login):
        self.type(self.LAST_NAME, lastname_login)

    def insert_address_login(self, address_login):
        self.type(self.ADDRESS_FIELD_LOGIN_INFO, address_login)

    def insert_city_login(self, city_login):
        self.type(self.CITY_FIELD_LOGIN_INFO, city_login)

    def insert_state_login(self, state_login):
        self.type(self.STATE_FIELD_LOGIN_INFO, state_login)

    def insert_zipcode_login(self, zip):
        self.type(self.ZIPCODE_FIELD_LOGIN_INFO, zip)

    def insert_ssn_login(self, ssn_login):
        self.type(self.SSN_FIELD_LOGIN_INFO, ssn_login)

    def display_credentials(self):
        assert self.is_displayed(self.USERNAME_FOUND) and self.is_displayed(self.PASSWORD_FOUND)
