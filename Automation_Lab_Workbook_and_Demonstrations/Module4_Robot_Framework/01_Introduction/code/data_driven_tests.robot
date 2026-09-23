*** Settings ***
Library    SeleniumLibrary
Test Template    Verify Website Content

Suite Setup       Open Browser    https://www.selenium.dev/    chrome
Suite Teardown    Close All Browsers
Test Teardown     Capture Page Screenshot    ${EXECDIR}/01_Introduction/screenshots/${TEST NAME}.png


*** Test Cases ***    Expected Text
Selenium Homepage     Selenium
Selenium Website      Selenium


*** Keywords ***
Verify Website Content
    [Arguments]    ${expected_text}
    Page Should Contain    ${expected_text}