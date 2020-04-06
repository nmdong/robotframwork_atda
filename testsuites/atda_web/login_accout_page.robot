
*** Settings *** 
Library    ../../apps/atda_web/atda_keywords.py       WITH NAME    browser_01

Test Teardown    browser_01.Close Browser
*** Variables ***
${url}    http://10.128.220.229:81/login

*** Test Cases ***
Login user
    Log To Console    Start Login user
    Log To Console    1. Launch new browser and go to address(http://10.128.220.229:81/login).
    browser_01.Open Browser    ${url}
    
    Log To Console    2. Verify login page.  
    browser_01.Verify Login Page
    browser_01.Login User Page    dong    123
    
    Log To Console    3. Login user.
    browser_01.Verify Login User