# Module 4 — Robot Framework

## Objective

Learn Robot Framework for keyword-driven, data-driven, and readable automation testing using SeleniumLibrary.

This module focuses on practical browser automation, reusable keywords, Page Object-style resources, test execution methods, reporting, and maintainable test structure.

---

## Module Structure

```text
Module4_Robot_Framework/
│
├── 01_Introduction/
│   ├── code/
│   ├── screenshots/
│   └── README.md
│
├── 02_Script_Running_Options/
│   ├── code/
│   ├── reports/
│   └── README.md
│
├── 03_Readability_Keywords_and_Page_Objects/
│   ├── tests/
│   ├── resources/
│   ├── pages/
│   ├── screenshots/
│   └── README.md
│
├── README.md
└── .gitignore
```

---

## Syllabus Coverage

### 01 — Introduction

* Robot Framework introduction
* Environment setup
* Basic `.robot` test cases
* SeleniumLibrary
* Keywords and test cases
* Data-driven testing using Test Template
* Automatic screenshot capture
* Robot Framework execution and reports

**Status: Completed ✅**

### 02 — Script Running Options

* Command Window execution
* `robot` command
* `pybot` legacy command awareness
* Running individual tests
* Running multiple suites
* CLI options
* Batch file execution
* Windows Task Scheduler concept
* Sauce Labs execution concept
* Jenkins execution concept

**Status: Completed ✅**

### 03 — Readability, Keywords and Page Objects

* Procedural test style
* Gherkin-like readability
* User-defined keywords
* Resource files
* Setup and teardown
* Reusable Selenium keywords
* Page Object-style resource
* Stable locators
* Automatic screenshots

**Status: Completed ✅**

---

## Technologies

* Python 3.14.7
* Robot Framework 7.5
* SeleniumLibrary 6.9.0
* Selenium WebDriver
* Google Chrome
* Windows PowerShell

---

## Execution

Activate the Module 4 virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run a Robot test:

```powershell
robot path\to\test.robot
```

Example:

```powershell
robot .\01_Introduction\code\basic_robot_tests.robot
```

Batch execution:

```powershell
.\02_Script_Running_Options\code\run_robot_tests.bat
```

---

## Reports and Evidence

Robot Framework automatically generates:

* `output.xml`
* `log.html`
* `report.html`

Practical tests also capture screenshots after execution for visual evidence.

Screenshots and reports help demonstrate successful automation execution in the GitHub project and academic/project documentation.

---

## Key Learning Outcomes

After completing this module, the learner can:

* Create Robot Framework test cases.
* Use SeleniumLibrary for browser automation.
* Create reusable user-defined keywords.
* Apply data-driven testing.
* Separate test logic from reusable resources.
* Build a lightweight Page Object-style structure.
* Use setup and teardown effectively.
* Execute Robot tests using different methods.
* Generate and inspect Robot Framework reports.
* Capture screenshot evidence from automated tests.
* Write readable and maintainable automation tests.



## Overall Status

**Module 4 — Robot Framework: Completed ✅**
