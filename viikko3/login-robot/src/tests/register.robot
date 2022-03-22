*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  guggu  kalle123

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi  testi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  guggu  kalle123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  mo  testi123
    Output Should Contain  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  username  pas
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  salla  password
    Output Should Contain  Password can't contain only letters