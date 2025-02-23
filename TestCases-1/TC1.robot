*** Settings ***
Library    SeleniumLibrary
Resource    TC1_Variables.robot
Resource    TC1_Keywords.robot

*** Test Cases ***
LoginTest
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    LoginToApp  
    Close Browser



    

