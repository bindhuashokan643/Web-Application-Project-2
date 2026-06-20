OrangeHRM Automation Testing Framework

Project Overview

This project automates the testing of the OrangeHRM Web Application using Selenium WebDriver with Python, PyTest, and Page Object Model (POM) Design Pattern



Technology Stack

* Python
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* WebDriver Manager
* Allure Reporting
* Jenkins Integration
* Excel Data Driven Testing (DDT)



Project Structure

Web_Application/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── admin_page.py
│   ├── myinfo_page.py
│   ├── leave_page.py
│   ├── claim_page.py
│   └── forgot_page.py
│
├── tests/
│   ├── test_testcase_01.py
│   ├── test_testcase_02.py
│   ├── test_testcase_03.py
│   ├── test_testcase_04.py
│   ├── test_testcase_05.py
│   ├── test_testcase_06.py
│   ├── test_testcase_07.py
│   ├── test_testcase_08.py
│   ├── test_testcase_09.py
│   └── test_testcase_10.py
│
├── testdata/
│   └── LoginData.xlsx
│
├── utilities/
│   ├── config.py
│   ├── excel_reader.py
│   ├── screenshot.py
│
├── reports/
│
│
├── allure-results/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── main.py


Test Cases Covered

TC01 : Validate Application URL

TC02 : Validate Application Title

TC03 : Validate Login Page Elements

TC04 : Validate Login Button Functionality

TC05 : Validate Forgot Password Navigation

TC06 : Validate Successful Login

TC07 : Validate Invalid Login

TC08 : Validate My Info Module

TC09 : Assign Leave Request

TC10 : Validate Claim Module Navigation and Assign Claim Page





Design Pattern Used

Page Object Model (POM)

Advantages:

* Reusable code
* Easy maintenance
* Better readability
* Reduced code duplication





Data Driven Testing

Test data is maintained in Excel files and read dynamically during execution.



Running the Tests

Run all tests:

pytest -v

Run a specific test:

pytest tests/test_testcase_10.py -v



Generate Allure Report

Execute tests:

pytest --alluredir=allure-results

Generate report:

allure serve allure-results



Jenkins Integration

1. Create Jenkins Job
2. Connect Git Repository
3. Configure Build Step
4. Execute:

pytest -v

5. Publish Allure Report



Observation for TC10

The OrangeHRM demo environment currently does not provide employee suggestions in the Assign Claim module.

Therefore:

* Navigation validation is automated.
* UI validation is automated.
* End-to-end claim submission cannot be completed due to unavailable employee master data in the demo environment.

This is an environment/data limitation and not a framework issue.




