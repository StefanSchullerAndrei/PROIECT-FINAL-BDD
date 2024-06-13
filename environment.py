from time import sleep
from driver import Driver
from pages.login_page import LoginPage
from pages.flip_ro_page import LoginPage_Flip
from pages.jules_faq import Faq
from pages.jules_sign_up_page import SignUp_Page
from pages.parabank_register_page import ParabankRegister_Page



def before_all(context):
    context.driver = Driver()
    context.login_page = LoginPage()
    context.flip_login_page = LoginPage_Flip()
    context.faq= Faq()
    context.sign_up_page = SignUp_Page()
    context.parabank_register_page = ParabankRegister_Page()
    context.saved_url = None

def after_all(context):
    context.driver.close()

