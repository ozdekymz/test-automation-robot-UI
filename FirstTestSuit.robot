*** Settings ***
Library     SeleniumLibrary
Resource    variables.robot

*** Test Cases ***
Login as User
    Open Browser    ${URL}   chrome
    Maximize Browser Window
    Input Text      id=username     ${USERNAME}
    Input Password  id=password     ${PASSWORD}
    Click Button    xpath=//button[@type='submit']  # Butonun XPath'i    
Verify Success Message
    ${message}=    Get Text    xpath=//div[@id='flash']
    Log           Message from page: ${message}             #Mesajı yazdır
    Should Contain     ${message}    ${SUCCESS_MESSAGE}