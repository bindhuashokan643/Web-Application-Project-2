from selenium.webdriver.support.wait import WebDriverWait
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

from utilities.config import BASE_URL


def test_testcase_06(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("Admin", "admin123")

    admin = AdminPage(driver)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(admin.ADMIN_MENU)
    ).click()

    assert "admin" in driver.current_url.lower() or \
           "Admin" in driver.page_source

    print("Admin User Management page opened successfully")