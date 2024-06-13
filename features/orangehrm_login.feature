Feature: Test the functionality of the LoginPage
  Background: Open Login Page
    Given I am on the Login Page
    @Incorrect.username
    Scenario: Check that "Invalid credentials" message is displayed when the user tries to login with incorrect username
      When I insert an incorrect username in the username input
      When I insert a correct password in the password input
      When I click Login button
      Then The main error message is displayed
      Then The error message contains "Invalid credentials"

    @Incorrect.password
    Scenario: Check that after inserting the correct username and password are redirecting to the main page of platform
      When I insert a correct username in the username input
      When I insert a incorrect password in the password input
      When I click Login button
      Then The main error message is displayed
      Then The error message contains "Invalid credentials"

    @Login.successfull
    Scenario: Check that after inserting the valid credentials and clicking login button, it will open the dashboard page
      When I insert a correct username in the username input
      When I insert a correct password in the password input
      When I click Login button
#      Then The dashboard page should be displayed
      Then I am on the Dashboard Page


