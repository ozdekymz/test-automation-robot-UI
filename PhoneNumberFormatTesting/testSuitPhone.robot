*** Settings ***
Library     SeleniumLibrary
Resource    variablesPhone.robot
Resource    keywordsPhone.robot

*** Comments ***
Description: Phone Number Validation
As a user, I want to have a Phone number validation control that will be checked by the system
as I start typing the values so that I can ensure right format for phone numbers are entered
by the user. "Test Template" is recommended to different combination testing.

*** Test Cases ***
LoginApp
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=username    timeout=10
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    id=kc-login
    Wait Until Element Is Visible    ${HAMBURGERICON}    timeout=10

NavigateOrderTab
    Wait Until Element Is Visible    ${HAMBURGERICON}    timeout=10
    Click Element   ${HAMBURGERICON}
    Wait Until Element Is Visible    ${EDITBUTTON}    timeout=10
#JS methodlarını execute etmemizi sağlar.
    Execute Javascript    return document.evaluate("(//li[@role='menuitem' and text()='Edit'])[1]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()


PhoneNumberValidation
    [Template]    Verify Phone Number Validation
    ${INVALID_PHONE_1}    ${ERROR_MSG_1}
    ${INVALID_PHONE_2}    ${ERROR_MSG_2}
    ${INVALID_PHONE_3}    ${ERROR_MSG_3}



    



