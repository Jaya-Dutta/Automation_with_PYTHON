*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary

Suite Setup       Open Browser    https://www.saucedemo.com/    chrome
Suite Teardown    Close All Browsers
Test Teardown     Capture Page Screenshot    ${EXECDIR}/Assignments/Assignment_1_Basic_Robot_Framework/screenshots/${TEST NAME}.png


*** Test Cases ***
Verify Login Result With Assertion
    [Documentation]    Perform login and verify the expected result.
    Input Text        id=user-name    standard_user
    Input Password    id=password     secret_sauce
    Click Button      id=login-button
    Page Should Contain    Products
    ${actual_title}=    Get Title
    Should Be Equal As Strings    ${actual_title}    Swag Labs

Verify API Response
    [Documentation]    Verify an API response using Should Be Equal As Strings.
    ${response}=    GET    https://jsonplaceholder.typicode.com/users/1
    Should Be Equal As Integers    ${response.status_code}    200
    ${status}=    Convert To String    ${response.status_code}
    Should Be Equal As Strings    ${status}    200