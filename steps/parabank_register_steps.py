import time

from behave import *

@given("I am on the home page")
def step_impl(context):
    context.parabank_register_page.navigate_to_page()
    time.sleep(0.5)

@when("I click Register button")
def step_impl(context):
    context.parabank_register_page.click_register_button()
    time.sleep(0.5)

@when('I insert my first name "{firstname}"')
def step_impl(context, firstname):
    context.parabank_register_page.insert_firstname(firstname)
    time.sleep(0.5)


@when('I insert my last name "{lastname}"')
def step_impl(context, lastname):
    context.parabank_register_page.insert_lastname(lastname)
    time.sleep(0.5)



@when('I insert my Address "{address}"')
def step_impl(context, address):
    context.parabank_register_page.insert_address(address)
    time.sleep(0.5)


@when('I insert my city "{city}"')
def step_impl(context, city):
    context.parabank_register_page.insert_city(city)
    time.sleep(0.5)

@when('I insert my state "{state}"')
def step_impl(context, state):
    context.parabank_register_page.insert_state(state)
    time.sleep(0.5)

@when('I insert my Zip Code "{zipcode}"')
def step_impl(context, zipcode):
    context.parabank_register_page.insert_zipcode(zipcode)
    time.sleep(0.5)

@when('I insert Phone # "{phonenumber}"')
def step_impl(context, phonenumber):
    context.parabank_register_page.insert_phonenumber(phonenumber)
    time.sleep(0.5)

@when('I insert my SSN "{SSN}"')
def step_impl(context, SSN):
    context.parabank_register_page.insert_ssn(SSN)
    time.sleep(0.5)

@when('I insert Username "{username}"')
def step_impl(context, username):
    context.parabank_register_page.insert_username(username)
    time.sleep(0.5)

@when('I insert Password "{password}"')
def step_impl(context, password):
    context.parabank_register_page.insert_password(password)
    time.sleep(0.5)

@when('I insert Confirm Password "{password}"')
def step_impl(context, password):
    context.parabank_register_page.insert_confirm_password(password)
    time.sleep(0.5)

@when('I click Register')
def step_impl(context):
    context.parabank_register_page.click_register()

@then('The message "Your account was created successfully. You are now logged in." is displayed. We found a problem')
def step_impl(context):
    context.parabank_register_page.error_register_credentials()
    time.sleep(0.5)

@then('I save the current URL')
def step_impl(context):
    context.saved_url = context.driver.current_url
    time.sleep(0.5)

@given('I am on the saved URL')
def step_impl(context):
    context.driver.get(context.saved_url)
    time.sleep(0.5)

@when('I click Log out button')
def step_impl(context):
    context.parabank_register_page.click_logout_button()
    time.sleep(0.5)

@when('I click Forgot login info button')
def step_impl(context):
    context.parabank_register_page.click_forgot_login_info_button()

@when('I click Find my login info button')
def step_impl(context):
    context.parabank_register_page.click_find_my_login_info_button()

@when('I insert first name "{firstname_login}"')
def step_impl(context, firstname_login):
    context.parabank_register_page.insert_firstname_login(firstname_login)
    time.sleep(0.5)

@when('I insert last name "{lastname_login}"')
def step_impl(context, lastname_login):
    context.parabank_register_page.insert_lastname_login(lastname_login)
    time.sleep(0.5)



@when('I insert Address "{address_login}"')
def step_impl(context, address_login):
    context.parabank_register_page.insert_address_login(address_login)
    time.sleep(0.5)


@when('I insert city "{city_login}"')
def step_impl(context, city_login):
    context.parabank_register_page.insert_city_login(city_login)
    time.sleep(0.5)

@when('I insert state "{state_login}"')
def step_impl(context, state_login):
    context.parabank_register_page.insert_state_login(state_login)
    time.sleep(0.5)

@when('I insert Zip Code "{zip}"')
def step_impl(context, zip):
    context.parabank_register_page.insert_zipcode_login(zip)
    time.sleep(0.5)

@when('I insert SSN "{ssn_login}"')
def step_impl(context, ssn_login):
    context.parabank_register_page.insert_ssn_login(ssn_login)

@then('It should display the username and password credentials')
def step_impl(context):
    context.parabank_register_page.display_credentials()
