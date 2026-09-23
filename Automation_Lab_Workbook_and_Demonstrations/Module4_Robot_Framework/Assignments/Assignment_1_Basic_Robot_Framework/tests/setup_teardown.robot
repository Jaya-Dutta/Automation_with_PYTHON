*** Settings ***
Library    SeleniumLibrary

Test Setup       Open Application And Login
Test Teardown    Logout And Cleanup
Suite Teardown   Close All Browsers


*** Test Cases ***
Verify Products Page After Login
    [Documentation]    Verify that the user reaches the Products page after login.
    Page Should Contain    Products

Verify Products Page Title
    [Documentation]    Verify the application title after login.
    Title Should Be    Swag Labs


*** Keywords ***
Open Application And Login
    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window
    Input Text        id=user-name    standard_user
    Input Password    id=password     secret_sauce
    Click Button      id=login-button
    Page Should Contain    Products

Logout And Cleanup
    [Documentation]    Log out and close the browser after each test.
    Click Button    id=react-burger-menu-btn
    Wait Until Element Is Visible    id=logout_sidebar_link    5s
    Click Element    id=logout_sidebar_link
    Page Should Contain Element    id=login-button
    Close All Browsers