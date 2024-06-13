from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Faq(BasePage):
    JULES_URL = "https://jules.app/sign-in"
    FAQ_BUTTON = (By.CSS_SELECTOR, 'a[class="jss17 jss20"]')
    JULES_FAQ_PAGE = "https://static.jules.app/faq.html"


    def navigate_to_sign_in_page(self):
        self.driver.get(self.JULES_URL)

    def click_on_faq(self):
        self.click(self.FAQ_BUTTON)

    def verify_faq_page(self, expected_url):
        current_url = self.driver.current_url
        print(f'Current URL: {current_url}')
        print(f'Expected URL: {expected_url}')


