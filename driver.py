
from time import sleep
import time

from selenium import webdriver


class Driver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    def close(self):
        time.sleep(5)
        self.driver.quit()