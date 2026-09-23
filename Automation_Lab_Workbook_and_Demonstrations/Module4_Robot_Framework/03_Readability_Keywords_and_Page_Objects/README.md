# 03 — Readability, Keywords and Page Objects

## Objective

This section demonstrates how Robot Framework test cases can be made readable, reusable, and maintainable by separating test logic, reusable keywords, and page-specific locators.

The implementation covers:

* Procedural and readable test styles
* Gherkin-like readability
* User-defined keywords
* Resource files
* Test Setup and Teardown
* Page Object Model
* Reusable locators
* Separation of test and page logic
* SeleniumLibrary integration
* Automatic screenshot capture

---

## Project Structure

```text id="2o7p4a"
03_Readability_Keywords_and_Page_Objects/
│
├── tests/
│   └── readable_login_tests.robot
│
├── resources/
│   └── common_keywords.resource
│
├── pages/
│   └── login_page.resource
│
├── screenshots/
│   └── Valid User Can Login Successfully.png
│
└── README.md
```

---

# 1. Why Readability Matters

Automation tests should be easy to understand for both technical and non-technical team members.

A low-level procedural test may contain implementation details:

```robot
Input Text    id=user-name    standard_user
Input Password    id=password    secret_sauce
Click Button    id=login-button
```

Although this works, the test contains page-specific implementation details.

A more readable approach is:

```robot
Login With Valid Credentials    standard_user    secret_sauce
Verify Successful Login
```

The second approach focuses on **what the test is validating** rather than how the browser interaction is implemented.

---

# 2. Gherkin-Like Readability

Robot Framework does not require Gherkin syntax, but Robot test cases can be written using descriptive keywords that provide a similar readable style.

Example:

```robot
*** Test Cases ***
Valid User Can Login Successfully
    Login With Valid Credentials    standard_user    secret_sauce
    Verify Successful Login
```

The test reads almost like a business scenario:

```text
Valid User Can Login Successfully
        ↓
Login With Valid Credentials
        ↓
Verify Successful Login
```

This improves communication between developers, testers, and other stakeholders.

---

# 3. User-Defined Keywords

Robot Framework allows custom keywords to be created from existing keywords.

Example:

```robot
Login With Valid Credentials
    [Arguments]    ${username}    ${password}
    Enter Username    ${username}
    Enter Password    ${password}
    Click Login
```

This combines several low-level browser actions into one reusable keyword.

Instead of repeating:

```text
Enter Username
Enter Password
Click Login
```

the test can simply use:

```text
Login With Valid Credentials
```

---

# 4. Resource Files

Reusable keywords and libraries can be stored in separate resource files.

The project uses:

```text id="q1oyz2"
resources/common_keywords.resource
```

The test imports the resource:

```robot
*** Settings ***
Resource    ../resources/common_keywords.resource
```

This keeps the test file smaller and separates reusable automation logic from individual test cases.

---

# 5. Page Object Resource

Page-specific locators are stored in:

```text id="qf7f1a"
pages/login_page.resource
```

Example:

```robot
*** Variables ***
${USERNAME_FIELD}    id=user-name
${PASSWORD_FIELD}    id=password
${LOGIN_BUTTON}      id=login-button
```

Page interactions are also defined in the same resource:

```robot
Enter Username
    [Arguments]    ${username}
    Input Text    ${USERNAME_FIELD}    ${username}

Enter Password
    [Arguments]    ${password}
    Input Password    ${PASSWORD_FIELD}    ${password}

Click Login
    Click Button    ${LOGIN_BUTTON}
```

The test does not need to know the actual locator values.

---

# 6. Page Object Architecture

The implementation follows a lightweight Page Object approach:

```text id="q2n3xr"
Test Case
    │
    ▼
Common Keywords
    │
    ▼
Login Page Resource
    │
    ├── Locators
    └── Page Actions
    │
    ▼
SeleniumLibrary
    │
    ▼
Chrome Browser
```

This separation provides better maintainability.

For example, if the username locator changes, the locator can be updated in:

```text
pages/login_page.resource
```

without changing the main test case.

---

# 7. Test Setup and Teardown

The test suite uses:

```robot
Test Setup       Open Login Page
Test Teardown    Capture Page Screenshot    ${EXECDIR}/03_Readability_Keywords_and_Page_Objects/screenshots/${TEST NAME}.png
Suite Teardown    Close All Browsers
```

### Test Setup

Runs before the test case and opens the browser.

### Test Teardown

Runs after the test case and captures a screenshot.

### Suite Teardown

Runs after the complete test suite and closes all browsers.

This provides a clean and reusable execution lifecycle.

---

# 8. Automatic Screenshot Evidence

Screenshots are automatically captured after the test.

The screenshots are stored in:

```text id="0m8x9n"
03_Readability_Keywords_and_Page_Objects/screenshots/
```

This provides visual execution evidence for:

* Successful browser automation
* Debugging
* Test documentation
* Academic/project presentation

---

# 9. Test Execution

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the test:

```powershell
robot .\03_Readability_Keywords_and_Page_Objects\tests\readable_login_tests.robot
```

---

# 10. Execution Result

The test was successfully executed using the Page Object and resource-file architecture.

```text
Valid User Can Login Successfully | PASS |
```

Final result:

```text
1 test, 1 passed, 0 failed
```

Robot Framework also generated its standard execution reports:

```text
output.xml
log.html
report.html
```

---

# 11. Benefits of This Structure

The lightweight architecture provides:

### Readability

Test cases describe business-level actions.

### Reusability

Common keywords can be reused across multiple test cases.

### Maintainability

Page-specific locators are centralized.

### Separation of Concerns

Test logic and browser/page implementation remain separate.

### Scalability

Additional page resources and reusable keywords can be added without making the test cases difficult to understand.

---

# Key Learning Outcomes

After completing this section, the following concepts have been practiced:

* Readable Robot Framework test cases
* Gherkin-like test readability
* User-defined keywords
* Resource files
* Page Object Model
* Page-specific locators
* Reusable browser actions
* Test Setup
* Test Teardown
* Suite Teardown
* SeleniumLibrary
* Automatic screenshots
* Maintainable Robot Framework architecture

---

## Status

**03 — Readability, Keywords and Page Objects: Completed ✅**
