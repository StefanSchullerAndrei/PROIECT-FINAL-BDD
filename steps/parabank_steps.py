import time

from behave import *

#Register

@given("I am on the home page")
def step_impl(context):
    context.parabank_page.navigate_to_page()

@when("I click Register button")
def step_impl(context):
    context.parabank_page.click_register_button()

@when('I insert my first name "{firstname}"')
def step_impl(context, firstname):
    context.parabank_page.insert_firstname(firstname)


@when('I insert my last name "{lastname}"')
def step_impl(context, lastname):
    context.parabank_page.insert_lastname(lastname)



@when('I insert my Address "{address}"')
def step_impl(context, address):
    context.parabank_page.insert_address(address)


@when('I insert my city "{city}"')
def step_impl(context, city):
    context.parabank_page.insert_city(city)

@when('I insert my state "{state}"')
def step_impl(context, state):
    context.parabank_page.insert_state(state)

@when('I insert my Zip Code "{zipcode}"')
def step_impl(context, zipcode):
    context.parabank_page.insert_zipcode(zipcode)

@when('I insert Phone # "{phonenumber}"')
def step_impl(context, phonenumber):
    context.parabank_page.insert_phonenumber(phonenumber)

@when('I insert my SSN "{SSN}"')
def step_impl(context, SSN):
    context.parabank_page.insert_ssn(SSN)

@when('I insert Username "{username}"')
def step_impl(context, username):
    context.parabank_page.insert_username(username)

@when('I insert Password "{password}"')
def step_impl(context, password):
    context.parabank_page.insert_password(password)

@when('I insert Confirm Password "{password}"')
def step_impl(context, password):
    context.parabank_page.insert_confirm_password(password)

@when('I click Register')
def step_impl(context):
    context.parabank_page.click_register()

@then('The message "Your account was created successfully. You are now logged in." is displayed. We found a problem')
def step_impl(context):
    context.parabank_page.error_register_credentials()

#Verify_username_exists

@then('It shows "This username alreardy exists" error')
def step_impl(context):
    context.parabank_page.verify_error()

#Verify login function

@when('I insert the username "{username}"')
def step_impl(context, username):
    context.parabank_page.insert_username_login(username)

@when('I insert the password "{password}"')
def step_impl(context, password):
    context.parabank_page.insert_password_login(password)

@when('I click Log in button')
def step_impl(context):
    context.parabank_page.login_button()

@then('It should appear a message "Welcome" and the Accounts Overview table')
def step_impl(context):
    context.parabank_page.welcome_message()

#Open new account

@when('I click Open New Account')
def step_impl(context):
    context.parabank_page.open_new_acc()

@when('I select the type of Account I want to open')
def step_impl(context):
    context.parabank_page.select_type_of_account()

@when('I select an existing account to transfer funds into the new account')
def step_impl(context):
    context.parabank_page.select_account()
    time.sleep(1)

@when('I click Open New Account button')
def step_impl(context):
    context.parabank_page.open_account_button()

@then('It appears the new account number')
def step_impl(context):
    context.parabank_page.open_account_number()

#Verify new account is created

@when('I click Accounts Overview')
def step_impl(context):
    context.parabank_page.account_overview_click()

@then('It should appear the new account ID opened in the table')
def step_impl(context):
    context.parabank_page.new_account_verified()

#Bill Pay

@when('I click Bill Pay from the menu')
def step_impl(context):
    context.parabank_page.bill_pay_button()

@when('I insert the credentials "{payee_name}", "{address}", "{city}", "{state}", "{zip_code}", "{phone_number}", "{account_number}", "{verify_account_number}"')
def step_impl(context, payee_name, address, city, state, zip_code, phone_number, account_number, verify_account_number):
    context.parabank_page.insert_payee_details(payee_name, address, city, state, zip_code, phone_number, account_number, verify_account_number)

@when('I type the ammount of money')
def step_impl(context):
    context.parabank_page.pay_money()

@when('I select the account')
def step_impl(context):
    context.parabank_page.select_payee_account()

@when('I select Send Payment button')
def step_impl(context):
    context.parabank_page.send_payment_button()

@then('It appears Bill Payment Complete')
def step_impl(context):
    context.parabank_page.verify_bill_payment_complete()

#Verify new balance

@then('Then It should appear the account used with less amount of money because of the bill')
def step_impl(context):
    context.parabank_page.verify_new_balance()

#Forgot login info
@then('I save the current URL')
def step_impl(context):
    context.saved_url = context.driver.current_url

@given('I am on the saved URL')
def step_impl(context):
    context.driver.get(context.saved_url)
    time.sleep(2)

@when('I click Log out button')
def step_impl(context):
    context.parabank_page.click_logout_button()

@when('I click Forgot login info button')
def step_impl(context):
    context.parabank_page.click_forgot_login_info_button()

@when('I click Find my login info button')
def step_impl(context):
    context.parabank_page.click_find_my_login_info_button()

@when('I insert first name "{firstname_login}"')
def step_impl(context, firstname_login):
    context.parabank_page.insert_firstname_login(firstname_login)

@when('I insert last name "{lastname_login}"')
def step_impl(context, lastname_login):
    context.parabank_page.insert_lastname_login(lastname_login)


@when('I insert Address "{address_login}"')
def step_impl(context, address_login):
    context.parabank_page.insert_address_login(address_login)


@when('I insert city "{city_login}"')
def step_impl(context, city_login):
    context.parabank_page.insert_city_login(city_login)


@when('I insert state "{state_login}"')
def step_impl(context, state_login):
    context.parabank_page.insert_state_login(state_login)

@when('I insert Zip Code "{zip}"')
def step_impl(context, zip):
    context.parabank_page.insert_zipcode_login(zip)

@when('I insert SSN "{ssn_login}"')
def step_impl(context, ssn_login):
    context.parabank_page.insert_ssn_login(ssn_login)

@then('It should display the username and password credentials')
def step_impl(context):
    context.parabank_page.display_credentials()

#Update contact info

@when('I click Update Contact Info')
def step_impl(context):
    context.parabank_page.click_update_contact_info()

@when('I change the last name with "{new_last_name}"')
def step_impl(context, new_last_name):
    context.parabank_page.update_last_name(new_last_name)

@when('I change the phone number with "{new_phone_number}"')
def step_impl(context, new_phone_number):
    context.parabank_page.update_phone_number(new_phone_number)

@when("I click Update profile")
def step_impl(context):
    context.parabank_page.click_update_profile()

@then('I receive errors about fields required to change')
def step_impl(context):
    context.parabank_page.profile_update_message()

#clear_database
@when('I click on Admin Page')
def step_impl(context):
    context.parabank_page.admin_page_click()

@when('I click on Clean')
def step_impl(context):
    context.parabank_page.clean_database_button()

@when('It appears a message that Database Cleaned')
def step_impl(context):
    context.parabank_page.database_cleaned_message()


@then('It will appear "The username and password could not be verified." message that no user was found')
def step_impl(context):
    context.parabank_page.no_user_found()

