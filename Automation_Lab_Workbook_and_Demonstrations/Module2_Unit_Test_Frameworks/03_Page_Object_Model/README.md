# 03 — Page Object Model

## Objective

Learn the Page Object Model (POM) design pattern and build a maintainable Selenium automation framework by separating test logic, page interactions, reusable utilities, configuration, and test data.

## Concepts Covered

This unit covers:

1. **Why to Have a Framework**

   * Need for a structured automation framework
   * Maintainability and reusability
   * Separation of test logic and application logic

2. **Framework Components**

   * Base class
   * Page classes
   * Test classes
   * Utility classes
   * Configuration file
   * Test data
   * Screenshots and reports

3. **What is Page Object Model**

   * Understanding the POM design pattern
   * Separating page locators and actions from test cases
   * Improving test readability and maintainability

4. **BasePage and Utility Concept**

   * Creating reusable Selenium methods
   * Centralizing common browser interactions
   * Using utility classes for common operations

5. **Inheriting BasePage Class**

   * Creating page-specific classes
   * Reusing methods from `BasePage`
   * Reducing duplicate Selenium code

6. **Utility to Read CSV Data**

   * Reading test data using Python's built-in `csv` module
   * Separating test data from test logic
   * Reusing external test data

7. **Convert Test Case to Page Object Model Framework**

   * Converting a traditional Selenium test into POM
   * Connecting test classes with page classes
   * Using configuration and external test data

8. **Taking Screenshots on Test Failure**

   * Detecting failed tests
   * Automatically capturing browser screenshots
   * Storing failure evidence in the `screenshots` directory

## Framework Architecture

The main execution flow is:

```text id="q0h2pz"
Test Class
    │
    ▼
Page Class
    │
    ▼
BasePage
    │
    ▼
Selenium WebDriver
```

Test data and configuration are handled separately:

```text id="c5h6xk"
test_login.py
    │
    ├── login_page.py
    │       └── base_page.py
    │
    ├── csv_reader.py
    │       └── login_data.csv
    │
    └── config.py
```

## Folder Structure

```text id="k8xw3m"
03_Page_Object_Model/
│
├── base/
│   └── base_page.py
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── utilities/
│   └── csv_reader.py
│
├── config/
│   └── config.py
│
├── test_data/
│   └── login_data.csv
│
├── screenshots/
│   └── failure screenshots
│
├── reports/
│   └── test reports, when required
│
└── README.md
```

## Key Learnings

* Understand the purpose and benefits of an automation framework.
* Implement the Page Object Model design pattern.
* Separate page actions from test cases.
* Create and inherit a reusable `BasePage`.
* Build page-specific classes.
* Read test data from CSV files.
* Centralize configuration and reusabl
