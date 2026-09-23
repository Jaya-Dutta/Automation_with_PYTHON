*** Settings ***
Resource    ../resources/common_keywords.resource

Test Setup       Open Login Page
Test Teardown    Capture Page Screenshot    ${EXECDIR}/03_Readability_Keywords_and_Page_Objects/screenshots/${TEST NAME}.png
Suite Teardown    Close All Browsers


*** Test Cases ***
Valid User Can Login Successfully
    [Documentation]    Verify that a valid user can log in successfully.
    Login With Valid Credentials    standard_user    secret_sauce
    Verify Successful Login
    