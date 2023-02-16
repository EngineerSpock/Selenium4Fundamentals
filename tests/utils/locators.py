from selenium.webdriver.common.by import By


class AboutPageLocators:
    PageHeader = (By.NAME, 'about_title')


class DeliveryPageLocators:
    PageHeader = (By.NAME, 'delivery_title')
    AboutPageLink = (By.LINK_TEXT, 'About company')


class FavoritesPageLocators:
    @staticmethod
    def product_link(product_id):
        return By.XPATH, f'//*[@id="product{product_id}"]/h5/a'

    REMOVE = (By.NAME, 'remove')


class MainPageLocators:
    CITY = (By.ID, 'select')
    COMPARISON = (By.NAME, 'comparison')
    SEARCH = (By.ID, 'search_product')
    CART = (By.NAME, 'goToBasket')
    FAVORITES = (By.NAME, 'favorites')
    SELECT_MENU = (By.ID, 'goToSelection')
    SELECT_MENU_CAR_BATTERIES = (By.ID, 'carBatteries')
    PageHeader = (By.ID, 'main_title')
    DeliveryPageLink = (By.LINK_TEXT, 'Payment and delivery')

    @staticmethod
    def add_to_cart(product_id):
        return By.XPATH, f'//*[@id="product{product_id}"]/div[3]/button[1]'

    @staticmethod
    def add_to_comparison(product_id):
        return (By.XPATH, f'//*[@id="product{product_id}"]/div[3]/button[2]')

    @staticmethod
    def add_to_favorites(product_id):
        return (By.XPATH, f'//*[@id="product{product_id}"]/div[3]/button[3]')

    @staticmethod
    def product_link(product_id):
        return (By.XPATH, f'//*[@id="product{product_id}"]/h5/a')

    @staticmethod
    def product_by_id(id):
        return (By.ID, f'product{id}')
