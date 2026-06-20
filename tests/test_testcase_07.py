from pages.forgot_page import ForgotPage
from utilities.config import  Forgot_Password_URL


def test_tc07_forgot_password(driver):

    driver.get(Forgot_Password_URL)
    forgot = ForgotPage(driver)

    forgot.enter_username("Admin")

    print("Username entered")

    forgot.click_reset()
    print(driver.current_url)
    print("Reset button clicked")

    assert "requestResetPassword" in driver.current_url

    print("Forgot Password Request Submitted Successfully")
