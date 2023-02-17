from selenium.webdriver import Keys
from tests.pages.about_page import AboutPage
from tests.pages.delivery_page import DeliveryPage
from tests.pages.favorites_page import FavoritesPage
from tests.pages.main_page import MainPage


def test_searching_returns_correct_product(browser, root_url):
    main_page = MainPage.navigate(browser)
    main_page.search_for('SOLITE' + Keys.ENTER)

    assert main_page.get_product_name(1).startswith('Battery SOLITE')


def test_can_add_and_remove_favorites(browser, root_url):
    prod_id = 1

    main_page = MainPage.navigate(browser)
    product_name = main_page.go_to_car_batteries()\
        .add_to_favorites(prod_id)\
        .get_product_name(prod_id)

    favorites_page = main_page.go_to_favorites()

    product_name_in_favorites = favorites_page.get_product_name(prod_id)
    favorites_page.remove_first()

    assert product_name == product_name_in_favorites
    assert favorites_page.is_empty()


def test_page_titles_are_correct(browser, root_url):
    main_page = MainPage.navigate(browser)

    main_page_header = main_page.get_header()
    delivery_page = main_page.go_to_delivery()

    delivery_page_header = delivery_page.get_header()
    about_page = delivery_page.go_to_about_page()

    about_page_header = about_page.get_header()

    assert main_page_header == 'Batteries online store'
    assert delivery_page_header == 'Payment and shipping Information'
    assert about_page_header == 'Information about our company'
