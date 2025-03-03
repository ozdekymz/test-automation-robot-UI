*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${BROWSER}  chrome
${URL}      https://osiris-ui.test.dbssuk.com/ui/osiris-ui/
${USERNAME}     ozdekaymaz123
${PASSWORD}     ozdekaymaz123
${HAMBURGERICON}    xpath= //*[@id="root"]/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[11]/button
${EDITBUTTON}       xpath= (//li[@role="menuitem" and .="Edit"])[1]
${ORDERCONTACTPHONENUMBER}   id=:re:
${MESSAGE}  xpath=//*[@id="simple-tabpanel-0"]/div[1]/div/div/div/div/div/div/div[1]/h3/div/div[2]/div[4]/div/div/div[2]/p

${INVALID_PHONE_1}     012345
${ERROR_MSG_1}         If a phone number starts with 0, it should be between 10 or 11 digits.

${INVALID_PHONE_2}     +90123
${ERROR_MSG_2}         If a phone number is international (i.e., starting with a code other than +44), it should be between 8 and 16 digits.

${INVALID_PHONE_3}     +4467898765412
${ERROR_MSG_3}         If a phone number starts with +44, it should be between 12 or 13 digits.

