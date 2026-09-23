*** Settings ***
Library    SeleniumLibrary
Resource   ../pages/login_page.resource


*** Keywords ***
Open Login Page
    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window

Login With Valid Credentials
    [Arguments]    ${username}    ${password}
    Enter Username    ${username}
    Enter Password    ${password}
    Click Login

Verify Successful Login
    Page Should Contain    Products