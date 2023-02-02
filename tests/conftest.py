import json
import os
import pytest as pytest
from selenium import webdriver
from config.definitions import ROOT_DIR


@pytest.fixture
def root_url():
    return os.path.join(ROOT_DIR, 'store', 'index.html')


def get_config_file_path():
    return os.path.join(ROOT_DIR, 'config', 'tests_config.json')


@pytest.fixture
def config(scope='session'):
    with open(get_config_file_path()) as config_file:
        config = json.load(config_file)

    return config


def set_options(opts, config):
    if config['mode'] == 'Headless':
        opts.add_argument('--headless=new')
    opts.page_load_strategy = config['page_load_strategy']


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        set_options(opts, config)
        driver = webdriver.Firefox(options=opts)
    elif config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        set_options(opts, config)
        driver = webdriver.Chrome(options=opts)
    elif config['browser'] == 'Edge':
        opts = webdriver.EdgeOptions()
        set_options(opts, config)
        driver = webdriver.Edge(options=opts)
    else:
        raise Exception(f'Unknown type of browser')

    driver.implicitly_wait(config['implicit_wait'])

    yield driver

    driver.quit()
