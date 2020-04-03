*** Settings *** 
Library    ../../apps/atda_web/atda_keywords.py       WITH NAME    browser_01
Library    ../../apps/atda_web/atda_keywords.py       WITH NAME    browser_02        

*** Variables ***
${url}    http://11.11.7.10/login

*** Test Cases ***
ATDA001 Account page - Verify create a new account with invalid information - WIN1
    Log To Console    Hello    
    browser_01.Open Browser       ${url}
    Sleep    5s    
    browser_01.Close Browser   
