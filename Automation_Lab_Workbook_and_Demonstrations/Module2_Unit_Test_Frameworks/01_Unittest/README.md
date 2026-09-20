# 01 — Unittest

## Objective

Learn the fundamentals of Python's built-in `unittest` framework and understand how to create, organize, execute, and validate automated test cases.

## Concepts Covered

This unit covers:

1. **Unittest Introduction**

   * Understanding the `unittest` framework
   * Test cases and test methods
   * Test discovery and execution

2. **First Test Case**

   * Creating a test class
   * Writing the first test method
   * Running a unittest test case

3. **Class-Level Setup and Teardown**

   * Using `setUpClass()`
   * Using `tearDownClass()`
   * Understanding one-time setup and cleanup for a test class

4. **Assert a Test Method**

   * Using unittest assertions
   * Validating expected vs actual results
   * Handling successful and failed assertions

5. **Create a Test Suite**

   * Grouping multiple test cases
   * Creating and executing a test suite

## Folder Structure

```text
01_Unittest/
│
├── code/
│   └── unittest test scripts
│
├── screenshots/
│   └── practical evidence, when required
│
├── reports/
│   └── test execution reports, when required
│
└── README.md
```

## Key Learnings

* Understand the structure of a Python `unittest` test case.
* Create test classes and test methods.
* Use `setUpClass()` and `tearDownClass()` for class-level setup and cleanup.
* Use assertions to validate expected results.
* Create and execute test suites.
* Interpret unittest execution results.

## How to Run

**From the Module 2 root directory:**

```powershell
cd "C:\Users\mail2\Automation_with_PYTHON\Automation_Lab_Workbook_and_Demonstrations\Module2_Unit_Test_Frameworks"
```

The Module 2 virtual environment is located at:

```text
Module2_Unit_Test_Frameworks\.venv
```

Activate it from the Module 2 root:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run an individual unittest file:

```powershell
python -m unittest .\01_Unittest\code\<test_file>.py
```

Run unittest discovery:

```powershell
python -m unittest discover -s .\01_Unittest\code
```

## Expected Output

A successful execution displays output similar to:

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.XXXs

OK
```

A failed assertion displays `FAIL` along with details about the failed test.

## Important Notes

* `unittest` is included in Python's standard library; no separate installation is required.
* Test classes should inherit from `unittest.TestCase`.
* Test methods normally use the `test_` prefix for automatic discovery.
* `setUpClass()` and `tearDownClass()` run once for a test class.
* Assertions determine whether a test passes or fails.
* Screenshots and reports are added only when required by the practical exercise.
