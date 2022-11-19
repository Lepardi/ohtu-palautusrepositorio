*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  petri
    Set Password  petri123
    Set Password_confirmation  petri123
    Submit Credentials
    Register Should Succeed

Register With Already Taken Username And Valid Password
    Set Username  kalle
    Set Password  kalle123
    Set Password_confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  petri123
    Set Password_confirmation  petri123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  petri
    Set Password  pe123
    Set Password_confirmation  pe123
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  petri
    Set Password  petri123
    Set Password_confirmation  petri1234
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  petri
    Set Password  petri123
    Set Password_confirmation  petri123
    Submit Credentials
    Go To Login Page
    Set Username  petri
    Set Password  petri123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  pe
    Set Password  petri123
    Set Password_confirmation  petri123
    Submit Credentials
    Go To Login Page
    Set Username  pe
    Set Password  petri123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
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

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open