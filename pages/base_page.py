import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            element_text = element.text
            if not element_text.strip():
                print(f"Element found by locator {locator} is empty.")
                return None
            return element_text
        except Exception as e:
            print(f"Error finding element by locator {locator}: {e}")
            return None

    def double_click_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
        except Exception as e:
            print(f"Error performing double-click on element by locator {locator}: {e}")










