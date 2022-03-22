*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Create User


***Test Cases***
Register With Valid Username And Password
    Set Username  maisa
    Set Password  koira123
    Set Password_confirmation  koira123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  koira123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  moira
    Set Password  ko
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kaali
    Set Password  koira123
    Set Password_confirmation  koira342
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  muumi
    Set Password  koira123
    Set Password_confirmation  koira123
    Submit Credentials
    Register Should Succeed
    Go To Login Page And Submit Credentials Login

Login After Failed Registration
    Set Username  kaulin
    Set Password  koira123
    Set Password_confirmation  koira123
    Submit Credentials
    Register Should Succeed
    Go To Login Page And Submit Credentials Login Fail

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Go To Register Page And Create User
    Go To Register Page
    Register Page Should Be Open

Go To Login Page And Submit Credentials Login
    Go To Login Page
    Set Username  muumi
    Set Password  koira123
    Submit Credentials Login
    Login Should Succeed

Go To Login Page And Submit Credentials Login Fail
    Go To Login Page
    Set Username  kaulin
    Set Password  kala
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

