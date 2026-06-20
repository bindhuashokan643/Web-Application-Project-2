import pytest
from pages.login_page import LoginPage
from utilities.config import BASE_URL
from utilities.excel_reader import get_login_data

testdata = get_login_data(
    "testdata/LoginData.xlsx"
)

@pytest.mark.login
@pytest.mark.parametrize(
    "username,password,expected_result",
    testdata
)

def test_testcase_01(driver,username,password,expected_result ):

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login(username,password)

    if expected_result == "Pass":

        assert "dashboard" in driver.current_url.lower()

    else:
        error_msg = login.get_error_message()
        print("Error Message:",error_msg)
        assert error_msg == "Invalid credentials"
