*** Settings ***
Library    SeleniumLibrary

Suite Setup       Open Browser    https://www.selenium.dev/    chrome
Suite Teardown    Close All Browsers
Test Teardown     Capture Page Screenshot    ${EXECDIR}/02_Script_Running_Options/reports/${TEST NAME}.png


*** Test Cases ***
Verify Selenium Homepage
    [Documentation]    Verify Selenium homepage using a standalone execution demo.
    Title Should Be    Selenium

Verify Selenium Page Content
    [Documentation]    Verify Selenium page content.
    Page Should Contain    Selenium