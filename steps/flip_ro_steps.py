import time

from behave import *


@given('I am on Flip main page')
def step_impl(context):
    context.flip_login_page.navigate_to_login_page()
    time.sleep(1)

@when('I click Accept cookies')
def step_impl(context):
    context.flip_login_page.accept_cookies()
    time.sleep(1)

@when('I click Contul meu')
def step_impl(context):
    context.flip_login_page.click_contul_meu()
    time.sleep(1)

@when('I insert random email')
def step_impl(context):
    context.flip_login_page.input_random_email()
    time.sleep(1)

@when('I insert the password "{password}"')
def step_impl(context, password):
    context.flip_login_page.input_password(password)
    time.sleep(1)

@when('I click the login button')
def step_impl(context):
    context.flip_login_page.click_login_button()
    time.sleep(1)

@then('The "{message}" message is displayed')
def step_impl(context, message):
    context.flip_login_page.email_message_displayed(message)

@then('The "{error}" is displayed')
def step_impl(context, error):
    context.flip_login_page.error_message(error)

@when('I insert "{email}" in the e-mail address field')
def step_impl(context, email):
    context.flip_login_page.input_email(email)
    time.sleep(2)

@when('I insert "{password1}" in the password address field')
def step_impl(context, password1):
    context.flip_login_page.input_password_1(password1)

