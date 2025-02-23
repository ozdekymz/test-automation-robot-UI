*** Keywords ***
LoginToApp
    Input Text      id=username     ${USERNAME}
    Input Password  id=password     ${PASSWORD}
    Click Button    xpath=//button[@type='submit']  # Butonun XPath'i