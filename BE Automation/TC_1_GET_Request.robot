*** Settings ***
Library    RequestsLibrary
Library    Collections
*** Variables ***
${base_url}    http://restapi.demoqa.com
${city}    Delhi

*** Test Cases ***
Get_weatherInfo
    create session    mysession    ${base_url}
    ${response}=    get request    mysession    /utilities/weather/city/${city} //response contains headers status code eg.

    # Log To Console    ${response.status_code}
    # Log To Console    ${response.content}
    # Log To Console    ${response.headers}    //now we want to verify something, how we can verify that?

    #VALIDATIONS

    #Validation 1:    
    ${status_code}=    convert to string ${response.status_code} //we need to convert to this value to string format since the response returned as an integer value.
    Should Be Equal    ${status_code}    200

    #Validation 2:
    ${body}=    convert to string    ${response.content} //we need to convert to this
    Should Contain    ${body}    Delhi

    #Validation 3:
    ${contentTypeValue}=    Get From Dictionary    ${response.headers}   Content-Type
    Should Be Equal    ${contentTypeValue}    application/json

    




