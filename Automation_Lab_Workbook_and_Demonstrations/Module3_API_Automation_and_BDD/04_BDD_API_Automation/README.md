# 04 - BDD API Automation

This submodule covers Behaviour-Driven Development (BDD) for API automation using Behave and Requests.

## Objectives

* Understand BDD concepts
* Write API scenarios using Gherkin
* Use Feature and Scenario
* Implement Given, When and Then steps
* Integrate Behave with Requests
* Validate API responses
* Use Behave scenario hooks
* Execute BDD API tests

## Files

### `features/api.feature`

Contains the BDD API scenario written in Gherkin.

Covers:

* Feature
* Scenario
* Given
* When
* Then
* API response validation

### `features/steps/api_steps.py`

Contains Python step definitions for the Gherkin scenario.

Covers:

* API endpoint setup
* GET request
* Status-code validation
* JSON response validation

### `features/environment.py`

Contains Behave lifecycle hooks.

Covers:

* `before_scenario`
* `after_scenario`
* Scenario execution status

## Run

From the `04_BDD_API_Automation` directory:

```powershell
behave
```

To display captured output:

```powershell
behave --no-capture
```

## Result

BDD API automation executed successfully.

* Feature: Passed
* Scenario: Passed
* Steps: 4 Passed
* API response validation: Passed
* Scenario hooks: Passed
* Failed: 0
