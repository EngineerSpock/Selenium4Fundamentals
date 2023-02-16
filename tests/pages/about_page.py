from tests.pages.base_page import BasePage
from tests.utils.locators import AboutPageLocators as Locators


class AboutPage(BasePage):
    def get_header(self):
        return self.find_element(Locators.PageHeader).text
