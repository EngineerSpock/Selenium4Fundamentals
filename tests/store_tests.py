import os.path
import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.definitions import ROOT_DIR


def switch_to_another_handler(browser, original_page_handler):
    for window_handle in browser.window_handles:
        if window_handle != original_page_handler:
            browser.switch_to.window(window_handle)
            break


def test_interact_with_windows(browser, root_url):
    browser.get(root_url)
    browser.maximize_window()

    original_page_handler = browser.current_window_handle

    delivery_page_link = browser.find_element(By.LINK_TEXT, 'Payment and delivery')
    delivery_page_link.click()

    switch_to_another_handler(browser, original_page_handler)

    delivery_title = browser.find_element(By.NAME, 'delivery_title').text
    assert delivery_title == 'Payment and shipping Information'

    browser.close()
    browser.switch_to.window(original_page_handler)

    about_page = browser.find_element(By.LINK_TEXT, 'About company')
    about_page.click()

    switch_to_another_handler(browser, original_page_handler)

    about_title = browser.find_element(By.NAME, 'about_title').text
    assert about_title == 'Information about our company'

    browser.close()
    browser.switch_to.window(original_page_handler)

    main_title = browser.find_element(By.ID, 'main_title').text
    assert main_title == 'Batteries online store'


def test_searching_returns_correct_product(browser, root_url):
    browser.get(root_url)

    search_txt = 'SOLITE' + Keys.ENTER
    browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(search_txt)

    WebDriverWait(browser, timeout=5).until(EC.visibility_of_element_located((By.ID, 'product1')))
    product_name = browser.find_element(By.ID, 'product1').find_element(By.TAG_NAME, 'a').text

    assert product_name.startswith('Battery SOLITE')


def test_interactions(browser, root_url):
    browser.get(root_url)
    selector_city = browser.find_element(By.NAME, 'select')
    Select(selector_city).select_by_visible_text('London')

    assert selector_city.get_attribute('value') == 's3'

    browser.find_element(By.ID, 'product1').find_element(By.NAME, 'addToCart').click()
    browser.find_element(By.NAME, 'goToBasket').click()

    phone_number_input = browser.find_element(By.NAME, 'userPhoneNumber')
    phone_number_input.send_keys('12345678')

    assert phone_number_input.get_attribute('value') == '+712345678'

    terms_accepted = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox'][name='acceptTermsCheckbox']")
    terms_accepted.click()

    assert terms_accepted.is_selected()

    terms_accepted.click()
    assert terms_accepted.is_selected() is False

    accumulate_bonuses = browser.find_element(By.ID, 'no')
    spend_bonuses = browser.find_element(By.ID, 'yes')
    spend_bonuses.click()

    assert spend_bonuses.is_selected() and accumulate_bonuses.is_selected() is False

    accumulate_bonuses.click()
    assert spend_bonuses.is_selected() is False and accumulate_bonuses.is_selected()


def test_xpaths_to_comparison_button(browser, root_url):
    browser.get(root_url)

    cmp_button = browser.find_element(By.XPATH, "//*[@id='root']/section[1]/div[3]/div[2]/button[2]")
    assert cmp_button.text == 'Comparison'

    cmp_button = browser.find_element(By.XPATH, "/html/body/div/section[1]/div[3]/div[2]/button[2]")
    assert cmp_button.text == 'Comparison'

    cmp_button = browser.find_element(By.XPATH, "(//button[text()='Comparison']//ancestor::div[1]//child::button)[2]")
    assert cmp_button.text == 'Comparison'


def test_css_selectors(browser, root_url):
    browser.get(root_url)

    el1 = browser.find_element(By.CSS_SELECTOR, "button[name='favorites']")
    el2 = browser.find_element(By.CSS_SELECTOR, "button[class='sc-iBYQkv doKaoE']")
    el3 = browser.find_element(By.CSS_SELECTOR, "button.sc-iBYQkv.doKaoE")
    el4 = browser.find_element(By.CSS_SELECTOR, "button[name='favorites'][class='sc-iBYQkv doKaoE']")

    el5 = browser.find_element(By.CSS_SELECTOR, "button[id='goToSelection']")
    el6 = browser.find_element(By.CSS_SELECTOR, "#goToSelection")

    lst = [el1, el2, el3, el4, el5, el6]

    assert all(el is not None for el in lst)

def test_can_add_and_remove_favorites(headless_chrome, root_url):
    headless_chrome.get(root_url)
    headless_chrome.maximize_window()

    headless_chrome.find_element(By.PARTIAL_LINK_TEXT, 'selection').click()
    headless_chrome.find_element(By.ID, 'goToSelection').click()
    headless_chrome.find_element(By.ID, 'carBatteries').click()

    product_block = headless_chrome.find_element(By.ID, 'product1')
    product_name_adding_to_favorites = product_block.find_element(By.TAG_NAME, 'a').text
    product_block.find_element(By.NAME, 'addToFavorites').click()

    # browser.find_element(By.CLASS_NAME, 'sc-iBYQkv doKaoE').click()
    headless_chrome.find_element(By.NAME, 'favorites').click()

    product_name_in_favorites = headless_chrome.find_element(By.ID, 'product1') \
        .find_element(By.TAG_NAME, 'a').text

    assert product_name_adding_to_favorites == product_name_in_favorites

    time.sleep(2)
    headless_chrome.find_element(By.NAME, 'remove').click()
    time.sleep(2)

    with pytest.raises(NoSuchElementException):
        headless_chrome.find_element(By.ID, 'product1')


def test_page_titles_are_correct(browser, root_url):
    # service = Service(executable_path="C:\\WebDrivers\\chromedriver.exe")
    # browser = webdriver.Chrome(service=service)
    browser.maximize_window()

    browser.get(root_url)

    main_title = browser.find_element(By.ID, 'main_title')
    assert main_title.text == 'Batteries online store'

    time.sleep(2)

    delivery_page_link = browser.find_element(By.LINK_TEXT, 'Payment and delivery')
    delivery_page_link.click()

    delivery_title = browser.find_element(By.NAME, 'delivery_title')
    assert delivery_title.text == 'Payment and shipping Information'

    time.sleep(2)

    about_page = browser.find_element(By.LINK_TEXT, 'About company')
    about_page.click()

    about_title = browser.find_element(By.NAME, 'about_title')
    assert about_title.text == 'Information about our company'

    time.sleep(2)


@pytest.fixture
def headless_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    yield driver

    driver.quit()

