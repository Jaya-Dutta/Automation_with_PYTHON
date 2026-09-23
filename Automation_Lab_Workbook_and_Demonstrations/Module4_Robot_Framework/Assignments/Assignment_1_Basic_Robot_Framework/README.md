# Assignment 1 — Basic Robot Framework

## Objective

Implement fundamental Robot Framework automation concepts including basic syntax, variables, data-driven testing, custom Python keywords, assertions, setup and teardown, tags, parallel execution, reporting, and logging.

---

## Assignment Structure

```text
Assignment_1_Basic_Robot_Framework/
│
├── tests/
│   ├── basic_syntax.robot
│   ├── variables_and_data.robot
│   ├── custom_keywords.robot
│   ├── assertions_and_api.robot
│   ├── setup_teardown.robot
│   ├── tags_and_execution.robot
│   └── reports_and_logs.robot
│
├── resources/
├── libraries/
│   └── CustomKeywords.py
│
├── test_data/
│   └── login_data.csv
│
├── reports/
└── screenshots/
```

---

## 1. Basic Syntax and Keywords

Implemented:

* Browser opening and URL navigation
* `Input Text`
* `Page Should Contain Element`
* Basic Robot Framework test cases
* Automatic screenshot capture

Test file:

```text
tests/basic_syntax.robot
```

**Result: 3 tests passed, 0 failed ✅**

---

## 2. Variables and Data-Driven Automation

Implemented:

* Username and password variables
* External CSV test data
* Multiple data sets using the same test flow
* Reusable test execution

Files:

```text
tests/variables_and_data.robot
test_data/login_data.csv
```

**Result: Passed ✅**

---

## 3. Custom Keywords and Libraries

Implemented:

* Custom Python Robot Framework library
* `Calculate Sum` custom keyword
* Robot Framework `String` library
* BuiltIn mathematical operations
* Logging of calculated results

File:

```text
libraries/CustomKeywords.py
tests/custom_keywords.robot
```

**Result: 2 tests passed, 0 failed ✅**

---

## 4. Assertions and Verification

Implemented:

* UI assertions
* `Should Be Equal As Strings`
* API request verification
* HTTP status-code validation

Test file:

```text
tests/assertions_and_api.robot
```

**Result: 2 tests passed, 0 failed ✅**

---

## 5. Test Setup and Teardown

Implemented:

* Common test setup
* Browser opening
* Automatic login
* Test teardown
* Logout and cleanup
* Suite-level browser cleanup

Test file:

```text
tests/setup_teardown.robot
```

**Result: 2 tests passed, 0 failed ✅**

---

## 6. Tags and Test Execution

Implemented tags:

* `smoke`
* `critical`
* `regression`
* `login`
* `data`

Test execution included:

```powershell
robot --include smoke ...
```

```powershell
robot --exclude regression ...
```

Parallel execution was demonstrated using Pabot:

```powershell
pabot --processes 2 ...
```

**Results:**

* Normal execution: 4 passed
* Smoke execution: 2 passed
* Parallel execution: 4 passed

**Status: Completed ✅**

---

## 7. Reports and Logs

Implemented:

* `Log` keyword
* Custom execution messages
* Robot Framework XML output
* HTML log
* HTML report
* Automatic screenshots

Generated files:

```text
reports/
├── output.xml
├── log.html
└── report.html
```

**Result: 1 test passed, 0 failed ✅**

---

## Technologies Used

* Python 3.14.7
* Robot Framework 7.5
* SeleniumLibrary
* RequestsLibrary
* Pabot 5.2.2
* Google Chrome
* Windows PowerShell

---

## Applications Used

### SauceDemo

Used for browser-based UI automation practice:

```text
https://www.saucedemo.com/
```

### JSONPlaceholder

Used for API verification practice:

```text
https://jsonplaceholder.typicode.com/users/1
```

---

## Execution

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run an individual test:

```powershell
robot --outputdir .\Assignments\Assignment_1_Basic_Robot_Framework\reports .\Assignments\Assignment_1_Basic_Robot_Framework\tests\basic_syntax.robot
```

Run tests using tags:

```powershell
robot --include smoke ...
```

Run tests in parallel:

```powershell
pabot --processes 2 ...
```

---

## Evidence

The assignment produces:

* Robot Framework execution results
* `output.xml`
* `log.html`
* `report.html`
* Browser screenshots
* Console execution logs

These provide execution evidence for academic documentation and GitHub project presentation.

---

## Final Status

**Assignment 1 — Basic Robot Framework: Completed ✅**

All seven assignment requirements were implemented and successfully executed.
