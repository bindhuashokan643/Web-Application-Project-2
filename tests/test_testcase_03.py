import pytest
from pages.login_page import LoginPage
from utilities.config import BASE_URL


@pytest.mark.smoke
def test_validate_login_fields(driver):

    # Open Login Page
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    # Validate Username Field
    assert login_page.is_username_visible(), \
        "Username field is not visible or enabled"

    # Validate Password Field
    assert login_page.is_password_visible(), \
        "Password field is not visible or enabled"

    print("Username and Password fields are visible and enabled")