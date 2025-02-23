*** Settings ***   #we have to define referance libraries
Library    SeleniumLibrary
Resource    InputBox_Variables.robot

*** Test Cases ***
CheckingInputBox    #need to define test name 
    Open Browser    ${URL}   ${BROWSER}
    Maximize Browser Window
    Title Should Be     ${title}    #Verify the Title of The Page
    # Click Button    xpath=//*[@id="RememberMe"]
    ${"email_txt"}    Set Variable    id=Email    #we can set the variable without any resource file
    Element Should Be Visible    ${"email_txt"}
    Element Should Be Enabled    ${"email_txt"}

    Input Text    ${"email_txt"}    johndoe@vodafone.com
    Sleep    5
    Clear Element Text    ${"email_txt"} 
    Sleep    3
    Close Browser   
