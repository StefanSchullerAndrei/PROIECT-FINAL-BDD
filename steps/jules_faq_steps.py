import time

from behave import *

@Given('I want to read the FAQ')
def step_impl(context):
    context.faq.navigate_to_sign_in_page()
    time.sleep(2)

@When('I click on FAQ')
def step_impl(context):
    context.faq.click_on_faq()
    time.sleep(2)

@Then('I am on the FAQ Page')
def step_impl(context):
    expected_url = "https://static.jules.app/faq.html"
    context.faq.verify_faq_page(expected_url)
    time.sleep(2)