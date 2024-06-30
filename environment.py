from time import sleep
from driver import Driver

from pages.parabank_register_page import ParabankRegister_Page



def before_all(context):
    context.driver = Driver()
    context.parabank_register_page = ParabankRegister_Page()
    
def after_all(context):
    context.driver.close()

