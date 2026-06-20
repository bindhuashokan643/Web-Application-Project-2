from ssl import Options

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_server": False,
            "profile.password_manager_enabled": False
        }
    )

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )

    )
    driver.maximize_window()
    yield driver
    driver.quit()