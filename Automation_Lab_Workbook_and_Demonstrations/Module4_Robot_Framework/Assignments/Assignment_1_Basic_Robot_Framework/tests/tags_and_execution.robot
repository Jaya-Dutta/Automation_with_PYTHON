*** Settings ***
Library    OperatingSystem


*** Test Cases ***
Smoke Test
    [Tags]    smoke    critical
    Log    Running Smoke Test
    Should Be Equal As Strings    ${1}    1

Regression Test
    [Tags]    regression
    Log    Running Regression Test
    Should Be Equal As Strings    ${2}    2

Login Test
    [Tags]    smoke    login
    Log    Running Login Test
    Should Be Equal As Strings    ${3}    3

Data Validation Test
    [Tags]    regression    data
    Log    Running Data Validation Test
    Should Be Equal As Strings    ${4}    4
    