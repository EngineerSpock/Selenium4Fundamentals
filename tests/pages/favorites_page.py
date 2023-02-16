from selenium.common import TimeoutException
from tests.pages.base_page import BasePage
from tests.utils.locators import FavoritesPageLocators as Locators


class FavoritesPage(BasePage):
    def get_product_name(self, product_id):
        return self.find_element(Locators.product_link(product_id)).text

    def remove_first(self):
        self.click_on(Locators.REMOVE)

    def is_empty(self):
        try:
            self.find_element(Locators.product_link(1), timeout_sec=0)
            return False
        except TimeoutException as ex:
            print(ex)
            return True
