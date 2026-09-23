*** Settings ***
Library    ../libraries/CustomKeywords.py
Library    String


*** Test Cases ***
Calculate Sum Using Python Keyword
    [Documentation]    Use a custom Python keyword to calculate the sum.
    ${result}=    Calculate Sum    10    20
    Should Be Equal As Numbers    ${result}    30

Use BuiltIn String And Math Operations
    [Documentation]    Demonstrate Robot Framework BuiltIn and String operations.
    ${text}=    Set Variable    robot framework
    ${upper}=    Convert To Upper Case    ${text}
    Should Be Equal    ${upper}    ROBOT FRAMEWORK

    ${number}=    Evaluate    10 * 5
    Should Be Equal As Numbers    ${number}    50

    Log    String operation result: ${upper}
    Log    Mathematical operation result: ${number}