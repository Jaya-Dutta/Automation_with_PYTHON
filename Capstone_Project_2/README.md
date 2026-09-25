# Selenium Python Automation Framework

A scalable Selenium automation framework built with Python for testing the Automation Exercise e-commerce application.

The framework demonstrates Selenium WebDriver, PyTest, Python Unittest, Page Object Model (POM), configuration management, CSV-based test data, explicit waits, automatic screenshots, logging, HTML reporting, and headless execution.

## Project Objective

Develop a maintainable Selenium Python automation framework using:

- Selenium WebDriver
- PyTest
- Python Unittest
- Page Object Model
- Utility classes
- Configuration management
- CSV test data
- Explicit waits
- Automatic screenshots
- Logging
- HTML reporting
- Headless browser execution

## Application Under Test

Automation Exercise

Base URL:

https://automationexercise.com/

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.14.7 | Programming language |
| Selenium 4.49.0 | Browser automation |
| PyTest 9.1.1 | Test execution |
| Unittest | Unit testing demonstration |
| pytest-html 4.2.0 | HTML test reporting |
| Chrome | Browser |
| CSV | Test data management |
| Git | Version control |

## Project Structure

```text
Capstone_Project_2/
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── search_page.py
│   └── cart_page.py
│
├── test_data/
│   └── testdata.csv
│
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_cart.py
│   └── test_unittest_demo.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── csv_reader.py
│   ├── screenshot.py
│   └── logger.py
│
├── screenshots/
├── reports/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
