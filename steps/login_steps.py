from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


#Incorrect.username

@given("I am on the Login Page")
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when("I insert an incorrect username in the username input")
def step_impl(context):
    context.login_page.incorrect_username("aDmin1")

@when("I insert a correct password in the password input")
def step_impl(context):
    context.login_page.correct_password("admin123")

@when("I click Login button")
def step_impl(context):
    context.login_page.click_login_button()

@then("The main error message is displayed")
def step_impl(context):
    context.login_page.error_displayed()

@then('The error message contains "{message}"')
def step_impl(context, message):
    context.login_page.error_message(message)

#Incorrect password

@when("I insert a correct username in the username input")
def step_impl(context):
    context.login_page.correct_username("Admin")

@when("I insert a incorrect password in the password input")
def step_impl(context):
    context.login_page.incorrect_password("admn123")

#@Login.succesfull
@then("I am on the Dashboard Page")
def step_impl(context):
    context.login_page.redirect_to_the_dashboard_page()

#Dashboard Page






