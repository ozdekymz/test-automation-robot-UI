#How can we send the POST request?
*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}=  https://restapi.demoqa.com/customer

*** Test Cases ***
Put_CustomerRegistration
    Create Session    mysession    ${base_url}
    ${body}=    Create Dictionary    
    Post Request    mysession /register      


