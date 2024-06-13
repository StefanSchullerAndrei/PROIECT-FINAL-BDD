import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from driver import Driver
from selenium.webdriver.common.by import By


class BasePage(Driver):
    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        element = self.find(locator)
        print(f"Element text: {element.text}")
            # return self.find(locator).text










