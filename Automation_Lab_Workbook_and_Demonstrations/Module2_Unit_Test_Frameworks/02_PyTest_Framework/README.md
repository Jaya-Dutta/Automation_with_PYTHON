# 02 — PyTest Framework

## Objective

Learn the PyTest framework and use it to build, organize, execute, and report automated tests with Selenium.

## Concepts Covered

This unit covers:

1. **Introduction of PyTest**

   * Understanding PyTest
   * Advantages of PyTest
   * PyTest test execution model

2. **Installing PyTest and Naming Conventions**

   * Installing PyTest
   * Test file naming conventions
   * Test method naming conventions

3. **Test Files, Test Methods and Assertions**

   * Creating PyTest test files
   * Writing test methods
   * Using PyTest assertions

4. **Subsets and Test Suites**

   * Running selected tests
   * Running multiple test files
   * Organizing tests for controlled execution

5. **Fixtures and `conftest.py`**

   * Understanding fixtures
   * Setup and teardown using fixtures
   * Sharing fixtures through `conftest.py`

6. **PyTest Features**

   * Test discovery
   * Fixtures
   * Assertions
   * Markers
   * Parameterization
   * Selective test execution

7. **Run Multiple Test Cases**

   * Executing multiple test cases
   * Running complete test modules
   * Reviewing test execution results

8. **Moving Selenium Test to PyTest**

   * Converting a Selenium test into PyTest
   * Integrating Selenium WebDriver with PyTest
   * Using fixtures for browser setup and cleanup

9. **PyTest HTML Reports**

   * Installing `pytest-html`
   * Generating HTML test reports
   * Reviewing test execution results through the generated report

## Folder Structure

```text
02_PyTest_Framework/
│
├── code/
│   └── PyTest test scripts
│
├── screenshots/
│   └── practical evidence, when required
│
├── reports/
│   └── pytest_report.html
│
└── README.md
```

## Key Learnings

* Understand the PyTest framework and its execution model.
* Follow PyTest file and test naming conventions.
* Create test methods and use assertions.
* Execute individual tests, selected tests, and multiple test cases.
* Use fixtures and `conftest.py` for reusable setup and teardown.
* Use PyTest features such as markers and parameterization.
* Convert Selenium tests into PyTest tests.
* Generate and review HTML test execution reports.

## How to Run

**From the Module 2 root directory:**

```powershell
cd "C:\Users\mail2\Automation_with_PYTHON\Automation_Lab_Workbook_and_Demonstrations\Module2_Unit_Test_Frameworks"
```

Activate the Module 2 virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run all PyTest tests:

```powershell
pytest .\02_PyTest_Framework\code
```

Run a specific test file:

```powershell
pytest .\02_PyTest_Framework\code\<test_file>.py
```

Run a specific test method:

```powershell
pytest .\02_PyTest_Framework\code\<test_file>.py::<test_method>
```

Generate an HTML report:

```powershell
pytest .\02_PyTest_Framework\code --html=.\02_PyTest_Framework\reports\pytest_report.html --self-contained-html
```

## Expected Output

A successful PyTest execution displays output similar to:

```text
============================= test session starts =============================
collected 5 items

.....                                                                    [100%]

============================== 5 passed in 2.XXs ===============================
```

The HTML report is generated at:

```text
02_PyTest_Framework/reports/pytest_report.html
```

## Important Notes

* PyTest is installed in the Module 2 virtual environment.
* The current environment uses **PyTest 9.1.1**.
* Selenium tests use **Selenium 4.49.0**.
* HTML reporting uses **pytest-html 4.2.0**.
* PyTest test files should normally follow the `test_*.py` or `*_test.py` naming convention.
* Test methods should normally start with `test_`.
* `conftest.py` is used to define reusable fixtures without importing them into every test file.
* HTML reports should be generated only when required by the syllabus or practical execution.
