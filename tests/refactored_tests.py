import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.about_page import AboutPage
from tests.pages.delivery_page import DeliveryPage
from tests.pages.favorites_page import FavoritesPage
from tests.pages.main_page import MainPage


def test_searching_returns_correct_product(browser, root_url):
    main_page = MainPage(browser)
    main_page.navigate_to()
    main_page.search_for('SOLITE' + Keys.ENTER)

    assert main_page.get_product_name(1).startswith('Battery SOLITE')


def test_can_add_and_remove_favorites(browser, root_url):
    main_page = MainPage(browser)
    main_page.navigate_to()
    main_page.go_to_car_batteries()

    prod_id = 1
    product_name = main_page.get_product_name(prod_id)
    main_page.add_to_favorites(prod_id)

    main_page.go_to_favorites()

    favorites_page = FavoritesPage(browser)
    product_name_in_favorites = favorites_page.get_product_name(prod_id)
    favorites_page.remove_first()

    assert product_name == product_name_in_favorites
    assert favorites_page.is_empty()


def test_page_titles_are_correct(browser, root_url):
    main_page = MainPage(browser)
    main_page.navigate_to()

    main_page_header = main_page.get_header()
    main_page.go_to_delivery()

    delivery_page = DeliveryPage(browser)
    delivery_page_header = delivery_page.get_header()
    delivery_page.go_to_about_page()

    about_page = AboutPage(browser)
    about_page_header = about_page.get_header()

    assert main_page_header == 'Batteries online store'
    assert delivery_page_header == 'Payment and shipping Information'
    assert about_page_header == 'Information about our company'
