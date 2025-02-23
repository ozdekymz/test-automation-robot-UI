*** Settings ***
Library            SeleniumLibrary
Resource    radioButtons_Variables.robot
Resource    radioButtons_Keywords.robot

*** Test Cases ***
Testing Radio Buttons and Check Boxes
    OpenPage
    Select Radio Button    gender    Female    



