Feature: Check the functionality of the Register Page
  Background:

    @Register
    Scenario Outline: Check that "Your account was created successfully. You are now logged in." even if I put letters instead of numbers at SSN
      Given I am on the home page
      When I click Register button
      When I insert my first name "Andrei"
      When I insert my last name "Stefan"
      When I insert my Address "Str. Principala, nr.1"
      When I insert my city "Brasov"
      When I insert my state "Romania"
      When I insert my Zip Code "507055"
      When I insert Phone # "0722113344"
      When I insert my SSN "DA"
      When I insert Username "<username>"
      When I insert Password "<password>"
      When I insert Confirm Password "<password>"
      When I click Register
      Then The message "Your account was created successfully. You are now logged in." is displayed. We found a problem

      Examples:
        | username | password |
        | andrei   | andrei   |

    @Verify_username_exists
    Scenario Outline: Verify that you can't create a new account with same username
      When I click Log out button
      When I click Register button
      When I insert my first name "Andrei"
      When I insert my last name "Stefan"
      When I insert my Address "Str. Principala, nr.1"
      When I insert my city "Brasov"
      When I insert my state "Romania"
      When I insert my Zip Code "507055"
      When I insert Phone # "0722113344"
      When I insert my SSN "DA"
      When I insert Username "<username>"
      When I insert Password "<password>"
      When I insert Confirm Password "<password>"
      And I click Register
      Then It shows "This username alreardy exists" error

      Examples:
        | username | password |
        | andrei   | andrei   |

    @Verify_login_function
    Scenario Outline: Verify that after inserting username and password credentials it welcomes with username greetings
      When I insert the username "<username>"
      When I insert the password "<password>"
      And I click Log in button
      Then It should appear a message "Welcome" and the Accounts Overview table

      Examples:
        | username | password |
        | andrei   | andrei   |

     @Open_new_account
    Scenario: Check that Open New Account function retrieves an ID for the new created account
      When I click Open New Account
      When I select the type of Account I want to open
      When I select an existing account to transfer funds into the new account
      And I click Open New Account button
      Then It appears the new account number

    @Verify_new_account_is_created
    Scenario: Verify that the ID of the new account appears on the Accounts overview section
      When I click Accounts Overview
      Then It should appear the new account ID opened in the table

    @Bill_Pay
    Scenario Outline: Verify that Bill Pay function is working
      When I click Bill Pay from the menu
      When I insert the credentials "<Payee Name>", "<Address>", "<City>", "<State>", "<Zip code>", "<Phone #>", "<Account #>", "<Verify Account#>"
      When I type the ammount of money
      When I select the account
      And I select Send Payment button
      Then It appears Bill Payment Complete

    Examples:
      | Payee Name     | Address             | City     | State   | Zip code | Phone #    | Account # | Verify Account# |
      | Marius Popescu | Str.Principala nr.1 | Ploiesti | Romania | 627014   | 0725894156 | 18453     | 18453           |

#    @Verify_new_balance
#      Scenario: Verify that after paying the bill, the balance of the account used has dropped with the amount paid
#        When I click Accounts Overview
#        Then It should appear the account used with less amount of money because of the bill

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

#    @Update_contact_info
#    Scenario Outline: Verify if after pressing Update Profile button we receive an error
#      When I click Update Contact Info
#      When I change the last name with "Stefan-Schuller"
#      When I change the phone number with "0722145784"
#      And I click Update profile
#      Then I receive errors about fields required to change
#      When I click Log out button
#      When I insert the credentials "<username>" and "<password>"
#
#    Examples:
#        | username | password |
#        | andrei   | andrei   |

    @Clear_database
    Scenario Outline: Check that clean database function actually clears all the data introduced, including the account
      When I click on Admin Page
      When I click on Clean
      When It appears a message that Database Cleaned
      When I click Log out button
      When I insert the username "<username>"
      When I insert the password "<password>"
      And I click Log in button
      Then It will appear "The username and password could not be verified." message that no user was found

      Examples:
        | username | password |
        | andrei   | andrei   |