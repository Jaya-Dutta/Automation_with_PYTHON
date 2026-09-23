# 01 — Introduction to Robot Framework

## Objective

This section introduces the fundamentals of Robot Framework and demonstrates browser automation using SeleniumLibrary.

The examples cover:

* Robot Framework installation and environment setup
* Basic Robot Framework test cases
* SeleniumLibrary integration
* Browser automation
* Suite Setup and Suite Teardown
* User-defined keywords
* Data-driven testing using Test Templates
* Command-line test execution
* Automatic screenshot capture

---

## Environment

The examples were developed and executed using:

| Component        | Version                                 |
| ---------------- | --------------------------------------- |
| Python           | 3.14.7                                  |
| Robot Framework  | 7.5                                     |
| SeleniumLibrary  | 6.9.0                                   |
| Selenium         | Installed as SeleniumLibrary dependency |
| Operating System | Windows                                 |

A dedicated Python virtual environment is used:

```text
.venv
```

---

## Project Files

```text
01_Introduction/
│
├── code/
│   ├── basic_robot_tests.robot
│   └── data_driven_tests.robot
│
├── screenshots/
│   ├── Verify Selenium Website Title.png
│   ├── Verify Selenium Website.png
│   └── ...
│
└── README.md
```

---

## 1. Basic Robot Framework Test

### File

```text
code/basic_robot_tests.robot
```

This test demonstrates a simple SeleniumLibrary-based browser automation flow.

The test:

1. Opens the Selenium website in Chrome.
2. Verifies the page title.
3. Verifies page content.
4. Captures a screenshot after each test.
5. Closes the browser after the test suite finishes.

### Important Robot Framework sections

```robot
*** Settings ***
```

Defines libraries and test execution configuration.

```robot
*** Test Cases ***
```

Contains the actual test cases.

```robot
Suite Setup
```

Runs once before the test suite.

```robot
Suite Teardown
```

Runs once after the test suite.

```robot
Test Teardown
```

Runs after every individual test case.

---

## 2. SeleniumLibrary

SeleniumLibrary provides browser automation keywords for Robot Framework.

Examples used in this section include:

```text
Open Browser
Title Should Be
Page Should Contain
Capture Page Screenshot
Close All Browsers
```

This allows Robot Framework to control a real browser without writing Selenium WebDriver code directly in Python.

---

## 3. Data-Driven Testing

### File

```text
code/data_driven_tests.robot
```

The data-driven example demonstrates Robot Framework's Test Template feature.

Instead of duplicating the same test logic, a common keyword is executed with different test data.

Conceptually:

```text
Test Template
      │
      ├── Test Data 1
      │
      └── Test Data 2
```

This approach improves:

* Reusability
* Maintainability
* Test readability
* Reduction of duplicate test logic

Example:

```robot
*** Settings ***
Test Template    Verify Website Content
```

The reusable keyword receives the test data:

```robot
Verify Website Content
    [Arguments]    ${expected_text}
    Page Should Contain    ${expected_text}
```

---

## 4. Automatic Screenshots

Each test uses:

```robot
Test Teardown    Capture Page Screenshot
```

The screenshots are stored inside:

```text
01_Introduction/screenshots/
```

This provides visual evidence of the browser state after each test.

Screenshots are particularly useful when:

* A test fails
* Debugging browser automation
* Demonstrating project execution
* Preparing project documentation
* Presenting automation work in an academic or professional portfolio

---

## 5. Running the Tests

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the basic test:

```powershell
robot .\01_Introduction\code\basic_robot_tests.robot
```

Run the data-driven test:

```powershell
robot .\01_Introduction\code\data_driven_tests.robot
```

---

## 6. Test Execution Result

Both test suites were successfully executed.

### Basic Robot Tests

```text
2 tests, 2 passed, 0 failed
```

### Data-Driven Tests

```text
2 tests, 2 passed, 0 failed
```

This confirms that the Robot Framework environment, SeleniumLibrary integration, browser automation, test templates, and screenshot workflow are functioning correctly.

---

## 7. Robot Framework Generated Reports

Robot Framework automatically generates:

```text
output.xml
log.html
report.html
```

These files contain execution information and test results.

They can be opened after a test run to inspect:

* Test cases
* Pass/fail status
* Keyword execution
* Execution time
* Errors and failures
* Test-level details

---

## Key Learning Outcomes

After completing this section, the following Robot Framework concepts have been practiced:

* Robot Framework project structure
* Robot Framework syntax
* SeleniumLibrary
* Browser automation
* Test cases
* Suite Setup
* Suite Teardown
* Test Teardown
* User-defined keywords
* Test Templates
* Data-driven testing
* Command-line execution
* Automatic screenshots
* Robot Framework reports

---

## Status

**01 — Introduction: Completed ✅**
