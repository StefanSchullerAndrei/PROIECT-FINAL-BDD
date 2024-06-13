Feature: Jules Sign Up test
  Background:
    Given I want to sign up

    @sign_up
    Scenario: Check that "Please enter a valid email address." is displayed when an incorrect email in typed
      When I click the sign up button
      When I click personal jules account
      When I click continue button
      When I set my first name "Andrei"
      When I click continue button
      When I set my last name to "Stefan"
      When I click continue button
      When I set my email to "exemplu1"
      Then I verify if message "Please enter a valid email address." is displayed in the application

    @forgot.login.info
