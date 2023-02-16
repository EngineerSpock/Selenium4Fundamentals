from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.definitions import ROOT_URL


class BasePage(object):
    def __init__(self, driver, base_url=ROOT_URL):
        self.base_url = base_url
        self.driver = driver

    def find_element(self, locator, timeout_sec=10):
        return WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout_sec=10):
        return WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_all_elements_located(locator),
                                                             message=f"Can't find elements by locator {locator}")

    def click_on(self, locator, timeout_sec=10):
        self.find_element(locator, timeout_sec).click()

    def navigate_to(self, url=''):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def enter_txt(self, locator, txt):
        self.find_element(locator).send_keys(txt)

    def wait_until_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located(locator))
