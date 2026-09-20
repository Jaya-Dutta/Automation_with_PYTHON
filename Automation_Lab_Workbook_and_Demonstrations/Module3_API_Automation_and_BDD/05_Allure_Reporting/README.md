# 05 - Allure Reporting

This submodule covers Allure reporting for BDD API automation.

## Objectives

* Integrate Allure with Behave
* Generate Allure result files
* Generate an HTML report
* Understand Allure report structure
* View API test execution results

## Tools

* Behave
* allure-behave
* Allure CLI

## Output

### `reports/`

Contains raw Allure result files generated from the Behave test execution.

### `allure-report/`

Contains the generated Allure HTML report.

Important files include:

* `index.html`
* `summary.json`
* `test-results.json`
* `data/`

## Generate Results

From the `04_BDD_API_Automation` directory:

```powershell
behave -f allure_behave.formatter:AllureFormatter -o "..\05_Allure_Reporting\reports"
```

## Generate HTML Report

From the `04_BDD_API_Automation` directory:

```powershell
allure generate "..\05_Allure_Reporting\reports" -o "..\05_Allure_Reporting\allure-report"
```

## Open Report

```powershell
allure open "..\05_Allure_Reporting\allure-report"
```

## Result

Allure integration was successfully configured.

* Behave integration: Passed
* Allure result generation: Passed
* HTML report generation: Completed
* `index.html`: Generated
* API scenario: Passed
