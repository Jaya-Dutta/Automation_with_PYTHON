# Module 3 - API Automation and BDD

This module covers API automation, advanced API testing, MySQL integration, Behaviour-Driven Development (BDD), and Allure reporting using Python.

## Objectives

* Automate REST APIs using Python
* Work with HTTP methods and JSON data
* Handle API responses and exceptions
* Use sessions, headers, cookies and authentication patterns
* Integrate API automation with MySQL
* Write BDD scenarios using Gherkin and Behave
* Generate Allure test reports
* Use reusable external test data

## Technologies

* Python
* Requests
* Behave
* MySQL
* mysql-connector-python
* Allure
* JSON
* REST APIs

## Module Structure

### 01 - API Automation with Requests

Covers:

* REST and SOAP basics
* GET and POST requests
* JSON payloads and responses
* Status codes and headers
* Response handling
* PUT, PATCH and DELETE
* External JSON test data
* CRUD API automation

### 02 - Advanced API Automation

Covers:

* Response handling
* HTTP errors
* Exceptions
* `raise_for_status()`
* Streaming responses
* Headers and timeouts
* Environment variables
* Sessions
* Authentication patterns
* Cookies

### 03 - MySQL Integration

Covers:

* MySQL database connection
* SQL queries from Python
* Data retrieval
* Parameterized queries
* INSERT and DELETE operations
* Commit and verification
* Database test-data management

### 04 - BDD API Automation

Covers:

* BDD concepts
* Gherkin syntax
* Feature and Scenario
* Given, When, Then
* Behave step definitions
* API testing with Requests
* Scenario hooks
* API response validation

### 05 - Allure Reporting

Covers:

* Allure and Behave integration
* Allure result generation
* HTML report generation
* Test execution reporting
* Allure report structure

## Environment

This module uses its own Python virtual environment:

```text
.venv
```

Main dependencies:

```text
requests
behave
mysql-connector-python
allure-behave
```

Allure CLI is installed separately and used for report generation.

## Execution

API automation:

```powershell
python .\01_API_Automation_with_Requests\code\requests_basics.py
python .\01_API_Automation_with_Requests\code\api_crud.py
```

Advanced API automation:

```powershell
python .\02_Advanced_API_Automation\code\advanced_requests.py
python .\02_Advanced_API_Automation\code\auth_session_response.py
```

MySQL integration:

```powershell
python .\03_MySQL_Integration\code\mysql_api_data.py
```

BDD API automation:

```powershell
cd .\04_BDD_API_Automation
behave
```

Allure results:

```powershell
behave -f allure_behave.formatter:AllureFormatter -o "..\05_Allure_Reporting\reports"
```

Allure report:

```powershell
allure generate "..\05_Allure_Reporting\reports" -o "..\05_Allure_Reporting\allure-report"
```

## Completion Status

| Submodule                         | Status    |
| --------------------------------- | --------- |
| 01 - API Automation with Requests | Completed |
| 02 - Advanced API Automation      | Completed |
| 03 - MySQL Integration            | Completed |
| 04 - BDD API Automation           | Completed |
| 05 - Allure Reporting             | Completed |

## Assignments

The module also includes three practical assignments covering Selenium, Behave BDD, data-driven automation, and Page Object Model concepts.

### Assignment 1 - Selenium Python and Behave BDD

File:

```text
Assignments/assignment_1_behave_bdd.py
```

Covers:

* Selenium browser automation
* BDD-style Given, When and Then flow
* End-to-end login scenario
* Successful login validation
* Automatic execution screenshot

### Assignment 2 - Data-Driven Automation

File:

```text
Assignments/assignment_2_data_driven_behave.py
```

Covers:

* Data-driven API automation
* Multiple test-data combinations
* API request execution
* Status-code validation
* Response-data validation

### Assignment 3 - Selenium Page Object Model

File:

```text
Assignments/assignment_3_behave_pom.py
```

Covers:

* Selenium automation
* Page Object Model (POM)
* Page locators and actions
* BDD-style execution flow
* Login validation
* Automatic execution screenshot

### Assignment Screenshots

Successful Selenium execution screenshots are stored in:

```text
Assignments/screenshots/
```

## Assignment Completion Status

| Assignment                                | Status    |
| ----------------------------------------- | --------- |
| Assignment 1 - Selenium + BDD             | Completed |
| Assignment 2 - Data-Driven API Automation | Completed |
| Assignment 3 - Selenium POM + BDD         | Completed |

## Result

Module 3 API Automation and BDD has been completed with working API automation, database integration, BDD testing, and Allure reporting examples.
