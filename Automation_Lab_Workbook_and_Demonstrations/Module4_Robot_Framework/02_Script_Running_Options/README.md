# 02 — Script Running Options

## Objective

This section demonstrates different ways to execute Robot Framework automation scripts, from direct command-line execution to batch execution and CI-oriented workflows.

The practical implementation uses a Robot Framework test suite and a Windows batch file. Other execution approaches are documented for learning and real-world automation usage.

---

## Project Files

```text
02_Script_Running_Options/
│
├── code/
│   ├── execution_demo.robot
│   └── run_robot_tests.bat
│
├── reports/
│   ├── output.xml
│   ├── log.html
│   ├── report.html
│   ├── Verify Selenium Homepage.png
│   └── Verify Selenium Page Content.png
│
└── README.md
```

---

# 1. Running Robot Framework from Command Window

Robot Framework tests can be executed directly from PowerShell or Command Prompt.

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run a single Robot test suite:

```powershell
robot .\02_Script_Running_Options\code\execution_demo.robot
```

To store generated reports in a specific directory:

```powershell
robot --outputdir .\02_Script_Running_Options\reports .\02_Script_Running_Options\code\execution_demo.robot
```

Robot Framework generates:

```text
output.xml
log.html
report.html
```

---

# 2. Robot vs Pybot

Modern Robot Framework uses the `robot` command:

```powershell
robot test.robot
```

`pybot` was the older command used by previous Robot Framework versions.

For current Robot Framework projects, use:

```text
robot
```

instead of:

```text
pybot
```

---

# 3. Running from PyCharm

Robot Framework tests can also be executed from an IDE such as PyCharm.

Typical workflow:

1. Open the Robot Framework project in PyCharm.
2. Configure the project interpreter to use the `.venv` environment.
3. Open the `.robot` test file.
4. Open the integrated terminal if required.
5. Run the Robot Framework command.

Example:

```powershell
robot .\02_Script_Running_Options\code\execution_demo.robot
```

The test result is displayed in the terminal and Robot Framework generates its standard reports.

---

# 4. Running a Single Test Case

A complete `.robot` file can contain multiple test cases.

To run only one test case, use the `--test` option:

```powershell
robot --test "Verify Selenium Homepage" .\02_Script_Running_Options\code\execution_demo.robot
```

This is useful when debugging or developing a specific test.

---

# 5. Running Multiple Test Suites

Multiple Robot Framework files can be executed together.

Example:

```powershell
robot .\01_Introduction\code\basic_robot_tests.robot .\01_Introduction\code\data_driven_tests.robot
```

Robot Framework executes the supplied test suites in the same command.

A directory can also be provided when multiple Robot files need to be executed:

```powershell
robot .\01_Introduction\code
```

---

# 6. Useful Command-Line Options

Robot Framework provides many CLI options for controlling test execution.

### Specify output directory

```powershell
robot --outputdir .\reports .\test.robot
```

### Select tests by name

```powershell
robot --test "Test Name" .\test.robot
```

### Select tests by tag

```powershell
robot --include smoke .\test.robot
```

### Exclude a tag

```powershell
robot --exclude slow .\test.robot
```

### Set a variable

```powershell
robot --variable ENVIRONMENT:QA .\test.robot
```

### Generate a custom output file

```powershell
robot --output custom_output.xml .\test.robot
```

### Display Robot Framework help

```powershell
robot --help
```

These options make command-line execution flexible for local testing and automated environments.

---

# 7. Windows Batch File

The project includes:

```text
code/run_robot_tests.bat
```

The batch file activates the virtual environment and executes the Robot test with a dedicated output directory.

It can be started from PowerShell:

```powershell
.\02_Script_Running_Options\code\run_robot_tests.bat
```

This provides a simple one-command execution workflow.

---

# 8. Windows Task Scheduler

Robot Framework can be executed automatically using Windows Task Scheduler.

A typical workflow is:

```text
Task Scheduler
      ↓
Run .bat file
      ↓
Activate virtual environment
      ↓
Execute Robot tests
      ↓
Generate reports
```

Example batch file:

```text
run_robot_tests.bat
```

Task Scheduler can be configured to run the batch file:

* At a specific time
* Daily
* Weekly
* At system startup
* Based on other Windows triggers

For this training project, Task Scheduler is documented as a concept rather than configured as a permanent scheduled task.

---

# 9. Sauce Labs

Robot Framework can be used with cloud browser platforms such as Sauce Labs for remote browser execution.

The recommended approach is to keep credentials outside the source code.

Environment variables:

```text
SAUCE_USERNAME
SAUCE_ACCESS_KEY
```

Example PowerShell configuration:

```powershell
$env:SAUCE_USERNAME="your_username"
$env:SAUCE_ACCESS_KEY="your_access_key"
```

Credentials should **never be hardcoded** inside `.robot` files or committed to GitHub.

A typical remote execution flow is:

```text
Robot Framework
      ↓
SeleniumLibrary
      ↓
Remote WebDriver
      ↓
Sauce Labs
      ↓
Cloud Browser
```

This project does not claim a Sauce Labs execution because remote execution requires an appropriate Sauce Labs account and configuration.

---

# 10. Jenkins

Robot Framework is commonly used in CI/CD pipelines.

A simplified Jenkins workflow is:

```text
Developer pushes code
        ↓
Jenkins job starts
        ↓
Environment is prepared
        ↓
Robot tests execute
        ↓
Robot reports are generated
        ↓
Results are published
```

A Jenkins job can execute a command such as:

```powershell
robot --outputdir reports .\02_Script_Running_Options\code\execution_demo.robot
```

Jenkins can then use the generated Robot Framework results for build/test reporting.

This project documents Jenkins integration conceptually rather than requiring a Jenkins server or CI infrastructure.

---

# 11. Execution Flow Used in This Project

The practical execution flow is:

```text
PowerShell
    ↓
Activate .venv
    ↓
robot / .bat
    ↓
SeleniumLibrary
    ↓
Chrome Browser
    ↓
Test Execution
    ↓
Screenshots
    ↓
Robot Reports
```

---

# 12. Execution Result

The practical execution demo was successfully verified.

```text
Execution Demo | PASS
2 tests, 2 passed, 0 failed
```

The batch file was also executed successfully:

```text
Execution Demo | PASS
2 tests, 2 passed, 0 failed
```

Generated reports were stored under:

```text
02_Script_Running_Options/reports/
```

Including:

```text
output.xml
log.html
report.html
```

Screenshots were also captured automatically after each test.

---

# Key Learning Outcomes

After completing this section, the following execution concepts have been practiced or documented:

* Command-line Robot execution
* `robot` command
* Legacy `pybot` concept
* Single test execution
* Multiple suite execution
* Robot Framework CLI options
* Batch file execution
* PyCharm execution workflow
* Windows Task Scheduler concept
* Sauce Labs remote execution concept
* Jenkins CI/CD execution concept
* Robot Framework reports
* Automated screenshot evidence

---

## Status

**02 — Script Running Options: Completed ✅**
