*** Settings ***
Library    SeleniumLibrary

Suite Setup       Open Browser    https://www.saucedemo.com/    chrome
Suite Teardown    Close All Browsers
Test Teardown     Capture Page Screenshot    ${EXECDIR}/Assignments/Assignment_1_Basic_Robot_Framework/screenshots/${TEST NAME}.png


*** Test Cases ***
Generate Report With Log Messages
    [Documentation]    Demonstrate custom log messages and HTML reporting.
    Log    Starting the SauceDemo verification test.
    
    Title Should Be    Swag Labs
    Log    Browser title verified successfully.

    Page Should Contain Element    id=user-name
    Log    Username field is present.

    Page Should Contain Element    id=password
    Log    Password field is present.

    Page Should Contain Element    id=login-button
    Log    Login button is present.

    Log    Test execution completed successfully.