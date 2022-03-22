*** Settings ***
Resource  resource.robot
Resource  login_resource.robot

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${WELCOME URL}  http://${SERVER}/welcome

*** Keywords ***

Login Should Succeed
    Main Page Should Be Open

Submit Credentials Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}