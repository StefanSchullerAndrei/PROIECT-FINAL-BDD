import time

from behave import *

@given("I want to sign up")
def step_impl(context):
    context.sign_up_page.navigate_to_sign_up()
    time.sleep(2)

@when("I click the sign up button")
def step_impl(context):
    context.sign_up_page.click_sign_up_button()
    time.sleep(2)

@when("I click personal jules account")
def step_impl(context):
    context.sign_up_page.click_option()
    time.sleep(2)

@when("I click continue button")
def step_impl(context):
    context.sign_up_page.click_continue_button()
    time.sleep(2)

@when('I set my first name "{firstname}"')
def step_impl(context, firstname):
    context.sign_up_page.set_first_name(firstname)
    time.sleep(1.5)

@when('I set my last name to "{lastname}"')
def step_impl(context, lastname):
    context.sign_up_page.set_last_name(lastname)
    time.sleep(2)

@when('I set my email to "{email}"')
def step_impl(context, email):
    context.sign_up_page.set_email(email)
    time.sleep(1.5)

@then('I verify if message "{error_message}" is displayed in the application')
def step_impl(context, error_message):
    context.sign_up_page.verify_message_displayed(error_message)
    time.sleep(1.5)

