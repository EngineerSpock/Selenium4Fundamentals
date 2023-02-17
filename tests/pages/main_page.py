from tests.pages.base_page import BasePage
from tests.pages.delivery_page import DeliveryPage
from tests.pages.favorites_page import FavoritesPage
from tests.utils.locators import MainPageLocators as Locators


class MainPage(BasePage):

    @staticmethod
    def navigate(driver):
        page = MainPage(driver)
        page.navigate_to()
        return page

    def get_header(self):
        return self.find_element(Locators.PageHeader).text

    def search_for(self, txt):
        self.enter_txt(Locators.SEARCH, txt)
        self.wait_until_visibility_of_element_located(Locators.product_by_id(1))
        return self

    def go_to_car_batteries(self):
        self.click_on(Locators.SELECT_MENU)
        self.click_on(Locators.SELECT_MENU_CAR_BATTERIES)
        return self

    def add_to_favorites(self, product_id):
        self.click_on(Locators.add_to_favorites(product_id))
        return self

    def add_to_cart(self, product_id):
        self.click_on(Locators.add_to_cart(product_id))
        return self

    def add_to_comparison(self, product_id):
        self.click_on(Locators.add_to_comparison(product_id))
        return self

    def go_to_favorites(self):
        self.click_on(Locators.FAVORITES)
        return FavoritesPage(self.driver)

    def go_to_delivery(self):
        self.click_on(Locators.DeliveryPageLink)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return DeliveryPage(self.driver)

    def get_product_name(self, product_id):
        return self.find_element(Locators.product_link(product_id)).text
