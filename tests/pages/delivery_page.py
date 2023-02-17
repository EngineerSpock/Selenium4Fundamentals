from tests.pages.about_page import AboutPage
from tests.pages.base_page import BasePage
from tests.utils.locators import DeliveryPageLocators as Locators


class DeliveryPage(BasePage):
    def get_header(self):
        return self.find_element(Locators.PageHeader).text

    def go_to_about_page(self):
        self.click_on(Locators.AboutPageLink)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return AboutPage(self.driver)
