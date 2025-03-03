*** Settings ***
Library     SeleniumLibrary
Resource    variablesPhone.robot

*** Comments ***
Arguments yaklaşımı ile aynı keyword farklı telefon numaraları ve hata mesajları ile tekrar tekrar çalıştırılabilir.

*** Keywords ***
Click Element With Javascript
    [Arguments]    ${locator}
    Execute Javascript    return document.evaluate("${locator}"), document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()

Wait For Element And Click With Javascript
    [Arguments]    ${locator}    ${timeout}=10
    Wait Until Element Is Visible    ${locator}    ${timeout}
    Click Element With Javascript    ${locator}


Verify Phone Number Validation
    [Arguments]    ${PHONE_NUMBER}    ${EXPECTED_MESSAGE}
    Wait Until Element Is Visible    ${ORDERCONTACTPHONENUMBER}    timeout=10
    Input Text    ${ORDERCONTACTPHONENUMBER}    ${PHONE_NUMBER}
    Wait Until Element Is Visible    ${MESSAGE}    timeout=15
    ${actual_message}=    Get Text    ${MESSAGE}
    Should Be Equal As Strings    ${actual_message}    ${EXPECTED_MESSAGE}