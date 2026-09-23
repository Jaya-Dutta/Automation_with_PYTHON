*** Settings ***
Library    SeleniumLibrary

Suite Setup       Open Browser    https://www.saucedemo.com/    chrome
Suite Teardown    Close All Browsers
Test Teardown     Capture Page Screenshot    ${EXECDIR}/Assignments/Assignment_1_Basic_Robot_Framework/screenshots/${TEST NAME}.png


*** Test Cases ***
Open SauceDemo Website
    [Documentation]    Open the browser and navigate to the SauceDemo website.
    Title Should Be    Swag Labs

Enter Username In Login Form
    [Documentation]    Use Input Text to enter a username.
    Input Text    id=user-name    standard_user
    Page Should Contain Element    id=user-name

Verify Login Elements
    [Documentation]    Verify that important login elements are present.
    Page Should Contain Element    id=user-name
    Page Should Contain Element    id=password
    Page Should Contain Element    id=login-button