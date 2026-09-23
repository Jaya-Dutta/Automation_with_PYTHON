*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    String

Suite Setup       Open Browser    https://www.saucedemo.com/    chrome
Suite Teardown    Close All Browsers
Test Teardown     Capture Page Screenshot    ${EXECDIR}/Assignments/Assignment_1_Basic_Robot_Framework/screenshots/${TEST NAME}.png


*** Variables ***
${VALID_USERNAME}    standard_user
${VALID_PASSWORD}    secret_sauce
${DATA_FILE}         ${EXECDIR}/Assignments/Assignment_1_Basic_Robot_Framework/test_data/login_data.csv


*** Test Cases ***
Login Using Variables
    [Documentation]    Use variables to store username and password.
    Input Text        id=user-name    ${VALID_USERNAME}
    Input Password    id=password     ${VALID_PASSWORD}
    Click Button      id=login-button
    Page Should Contain    Products

Login Using External Data
    [Documentation]    Read login data from an external CSV file.
    ${data}=    Get File    ${DATA_FILE}
    ${lines}=    Split To Lines    ${data}
    FOR    ${line}    IN    @{lines}[1:]
        ${parts}=    Split String    ${line}    ,
        Input Text        id=user-name    ${parts}[0]
        Input Password    id=password     ${parts}[1]
        Click Button      id=login-button
        Page Should Contain    Products
        Go To    https://www.saucedemo.com/
    END