*** Settings ***
Library    SeleniumLibrary

Suite Setup       Open Browser    https://www.selenium.dev/    chrome
Suite Teardown    Close All Browsers
Test Teardown     Capture Page Screenshot    ${EXECDIR}/01_Introduction/screenshots/${TEST NAME}.png


*** Test Cases ***
Verify Selenium Website Title
    [Documentation]    Verify that the Selenium website opens successfully.
    Title Should Be    Selenium

Verify Selenium Website
    [Documentation]    Verify that the Selenium homepage is displayed.
    Page Should Contain    Selenium