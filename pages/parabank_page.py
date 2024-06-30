import random
import re

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


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
    USERNAME_LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    PASSWORD_FIELD = (By.ID, 'customer.password')
    CONFIRM_PASSWORD_FIELD = (By.ID, 'repeatedPassword')
    REGISTER_BUTTON_CONFIRM = (By.CSS_SELECTOR, 'input[value="Register"]')
    USERNAME_EXISTS = (By.ID, "customer.username.errors")
    SSN_ERROR = (By.ID, 'customer.ssn.errors')
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, "a[href='logout.htm']")
    FORGOT_LOGIN_INFO_BUTTON = (By.XPATH, "//a[normalize-space()='Forgot login info?']")
    FIND_MY_LOGIN_INFO_BUTTON = (By.XPATH, "//input[@value='Find My Login Info']")
    USERNAME_FOUND = (By.XPATH, "//b[normalize-space()='Username']")
    PASSWORD_FOUND = (By.XPATH, "//b[normalize-space()='Password']")
    OPEN_NEW_ACC_MENU_BUTTON = (By.XPATH, "//a[normalize-space()='Open New Account']")
    TYPE_OF_ACCOUNT = (By.ID, "type")
    OPEN_ACC_BUTTON = (By.CSS_SELECTOR, "input[type='button']")
    ACCOUNT_NUMBER = (By.ID, "newAccountId")
    ACCOUNTS_OVERVIEW_BUTTON = (By.XPATH, "//a[normalize-space()='Accounts Overview']")
    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Log In']")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, "p[class='smallText'] b")
    ACCOUNT_OVERVIEW_TABLE = (By.ID, "accountTable")
    BILL_PAY_BUTTON = (By.XPATH, "//a[normalize-space()='Bill Pay']")
    PAYEE_NAME = (By.CSS_SELECTOR, "input[name='payee.name']")
    ADDRESS_PAYEE = (By.XPATH, "//input[@name='payee.address.street']")
    CITY_PAYEE = (By.CSS_SELECTOR, "input[name='payee.address.city']")
    STATE_PAYEE = (By.XPATH, "//input[@name='payee.address.state']")
    ZIP_CODE_PAYEE = (By.CSS_SELECTOR, "input[name='payee.address.zipCode']")
    PHONE_NR = (By.CSS_SELECTOR, "input[name='payee.phoneNumber']")
    ACCOUNT_PAYEE = (By.CSS_SELECTOR, "input[name='payee.accountNumber']")
    VERIFY_ACCOUNT = (By.XPATH, "//input[@name='verifyAccount']")
    AMOUNT_PAYEE = (By.CSS_SELECTOR, "input[name='amount']")
    MAIN_ACCOUNT_MONEY = (By.XPATH, "//tbody/tr[1]/td[2]")
    SEND_PAYMENT = (By.CSS_SELECTOR, "input[value='Send Payment']")
    BILL_PAYMENT_MESSAGE = (By.CSS_SELECTOR, "div[id='billpayResult'] h1[class='title']")
    UPDATE_CONTACT_INFO = (By.XPATH, "//a[normalize-space()='Update Contact Info']")
    UPDATE_PROFILE_BUTTON = (By.CSS_SELECTOR, "input[value='Update Profile']")
    UPDATE_LAST_NAME = (By.ID, "customer.lastName")
    UPDATE_PHONE_NUMBER = (By.ID, "customer.phoneNumber")
    ADMIN_PAGE = (By.XPATH, "//a[normalize-space()='Admin Page']")
    CLEAN_BUTTON = (By.CSS_SELECTOR, "button[value='CLEAN']")
    DATABASE_CLEAN_MESSAGE = (By.XPATH, "//b[normalize-space()='Database Cleaned']")
    ERROR_NO_USER = (By.XPATH, "//p[@class='error']")

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

    def verify_error(self):
        self.is_displayed(self.USERNAME_EXISTS)

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

    def open_new_acc(self):
        self.click(self.OPEN_NEW_ACC_MENU_BUTTON)

    def select_type_of_account(self):
        self.click(self.TYPE_OF_ACCOUNT)
        option1 = self.driver.find_element(By.XPATH, "//option[@value='0']")
        option2 = self.driver.find_element(By.XPATH, "//option[@value='1']")
        select_option = random.choice([option1, option2])
        select_option.click()

    def select_account(self):
        all_options = self.driver.find_elements(By.TAG_NAME, "option")
        select_option = random.choice(all_options)
        select_option.click()

    def open_account_button(self):
        self.click(self.OPEN_ACC_BUTTON)

    def verify_error(self):
        self.is_displayed(self.USERNAME_EXISTS)

    def insert_username_login(self, username):
        self.type(self.USERNAME_LOGIN_FIELD, username)

    def insert_password_login(self, password):
        self.type(self.PASSWORD_LOGIN_FIELD, password)

    def login_button(self):
        self.click(self.CUSTOMER_LOGIN_BUTTON)

    def welcome_message(self):
        self.is_displayed(self.WELCOME_MESSAGE)

    def open_account_number(self):
        self.is_displayed(self.ACCOUNT_NUMBER)
        new_account = self.driver.find_element(By.ID, "newAccountId")
        self.new_account = new_account.text

    def account_overview_click(self):
        self.click(self.ACCOUNTS_OVERVIEW_BUTTON)

    def new_account_verified(self):
        main_account_id = self.driver.find_element(By.XPATH, "//tr[1]/td[1]/a")
        self.main_account_id = main_account_id.text
        initial_balance = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]")
        self.initial_balance = initial_balance.text
        account_overview_text = self.get_text(self.ACCOUNT_OVERVIEW_TABLE)
        if account_overview_text is None:
            raise AssertionError("Account overview table text is None. Failed to retrieve the table content.")

        print(f"Account Overview Table Text: {account_overview_text}")  # Debugging output
        print(f"New Account ID: {self.new_account}")  # Debugging output

        assert self.new_account in account_overview_text, f"New account ID {self.new_account} not found in the account overview table"

    def bill_pay_button(self):
        self.click(self.BILL_PAY_BUTTON)

    def insert_payee_details(self, payee_name, address, city, state, zip_code, phone_number, account_number, verify_account_number):
        self.type(self.PAYEE_NAME, payee_name)
        self.type(self.ADDRESS_PAYEE, address)
        self.type(self.CITY_PAYEE, city)
        self.type(self.STATE_PAYEE, state)
        self.type(self.ZIP_CODE_PAYEE, zip_code)
        self.type(self.PHONE_NR, phone_number)
        self.type(self.ACCOUNT_PAYEE, account_number)
        self.type(self.VERIFY_ACCOUNT, verify_account_number)

    def pay_money(self):
        cleaned_account_money = re.sub(r'[^\d.]', '', self.initial_balance)

        # Convert the cleaned string to a float
        float_account_money = float(cleaned_account_money)

        # Convert the float to an integer for randint (since randint needs integer arguments)
        int_account_money = int(float_account_money)
        self.int_account_money = int_account_money

        random_amount = random.randint(1, int_account_money)
        self.type(self.AMOUNT_PAYEE, random_amount)
        self.random_amount_paid = random_amount

    def select_payee_account(self):
        # self.click(self.driver.find_element(By.CSS_SELECTOR, "select[name='fromAccountId']"))
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "fromAccountId")))
        select = Select(dropdown)
        select.select_by_visible_text(self.main_account_id)

    def send_payment_button(self):
        self.click(self.SEND_PAYMENT)

    def verify_bill_payment_complete(self):
        self.is_displayed(self.BILL_PAYMENT_MESSAGE)

    def verify_new_balance(self):
        initial_balance = self.int_account_money
        random_amount_paid = self.random_amount_paid
        final_balance = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]")
        self.final_balance = final_balance.text
        new_balance = re.sub(r'[^\d.]', '', self.final_balance)

        # Convert the cleaned string to a float
        float_new_balance = float(new_balance)

        # Convert the float to an integer for randint (since randint needs integer arguments)
        int_final_balance = int(float_new_balance)

        assert initial_balance is not None, "Initial balance was not retrieved."
        assert final_balance is not None, "Final balance was not retrieved."
        assert random_amount_paid is not None, "Random amount for bill payment was not saved."

        int_final_balance = initial_balance - random_amount_paid
        assert final_balance == int_final_balance, f"Expected balance to be {int_final_balance}, but got {final_balance}."
        print(f"Initial balance: {initial_balance}, Amount paid: {random_amount_paid}, Final balance: {final_balance}")

    def click_update_contact_info(self):
        self.click(self.UPDATE_CONTACT_INFO)

    def update_last_name(self, new_last_name):
        # self.driver.find_element(By.ID, "customer.lastName").clear()
        # self.type(self.UPDATE_LAST_NAME, new_last_name)

        try:
            last_name_field = self.driver.find_element(By.ID, "customer.lastName")
            last_name_field.clear()
            self.type(last_name_field, new_last_name)
        except Exception as e:
            print(f"Error updating last name: {e}")


    def update_phone_number(self, new_phone_number):
        # self.driver.find_element(By.ID, "customer.phoneNumber").clear()
        # self.type(self.UPDATE_PHONE_NUMBER, new_phone_number)

        try:
            phone_number_field = self.driver.find_element(By.ID, "customer.phoneNumber")
            phone_number_field.clear()
            self.type(phone_number_field, new_phone_number)
        except Exception as e:
            print(f"Error updating phone number: {e}")

    def click_update_profile(self):
        self.click(self.UPDATE_PROFILE_BUTTON)

    def profile_update_message(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "state-error")))
        self.is_displayed(self.driver.find_element(By.ID, "state-error"))

    def admin_page_click(self):
        self.click(self.ADMIN_PAGE)

    def clean_database_button(self):
        self.click(self.CLEAN_BUTTON)

    def database_cleaned_message(self):
        assert self.is_displayed(self.DATABASE_CLEAN_MESSAGE)

    def no_user_found(self):
        assert self.is_displayed(self.ERROR_NO_USER)


