Feature: Check the functionality of the Register Page
  Background:
    Given I am on the home page

    @Register
    Scenario: Check that "Your account was created successfully. You are now logged in." even if I put letters instead of numbers at SSN
      When I click Register button
      When I insert my first name "Andrei"
      When I insert my last name "Stefan"
      When I insert my Address "Str. Principala, nr.1"
      When I insert my city "Brasov"
      When I insert my state "Romania"
      When I insert my Zip Code "507055"
      When I insert Phone # "0722113344"
      When I insert my SSN "DA"
      When I insert Username "user"
      When I insert Password "password"
      When I insert Confirm Password "password"
      When I click Register
      Then The message "Your account was created successfully. You are now logged in." is displayed. We found a problem

    @Forgot_login_info
    Scenario: Check that Forgot login info actually retrieves username and password
      When I click Log out button
      When I click Forgot login info button
      When I insert first name "Andrei"
      When I insert last name "Stefan"
      When I insert Address "Str. Principala, nr.1"
      When I insert city "Brasov"
      When I insert state "Romania"
      When I insert Zip Code "507055"
      When I insert SSN "DA"
      And I click Find my login info button
      Then It should display the username and password credentials