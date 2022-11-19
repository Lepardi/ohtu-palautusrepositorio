*** Settings ***
Resource  resource.robot
Test Setup  Create User  kalle  kalle123

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  petri  petri123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ki  ki123456
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  petri  petri12
    Output Should Contain  Password too short

#Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  petri  joohuomentavaan
    Output Should Contain  Password should not contain only letters