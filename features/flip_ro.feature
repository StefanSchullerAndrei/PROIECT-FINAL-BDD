Feature: Check the functionality of FLIP.RO login page
  Given I am on Flip main page
    # Unregistered credentials attempt
    @flip1
    Scenario: Check "Aceasta adresa de email nu este asociata unui cont existent." message is displayed when I enter an unregistered e-mail address
#      Given I am on Flip main page
      When I click Accept cookies
      When I click Contul meu
      When I insert random email
      When I insert the password "password23"
      When I click the login button
      Then The "Aceasta adresa de email nu este asociata unui cont existent." message is displayed

    #No username and no password
    @flip2
    Scenario: Check that "Adresa de email lipseste" is displayed if no credentials are entered
#      Given I am on Flip main page
      When I click Accept cookies
      When I click Contul meu
      When I click the login button
      Then The "Adresa de e-mail lipseste." message is displayed

    #Username and one character password
    @flip3
    Scenario: Check "Parola trebuie sa aiba cel putin 6 caractere" message is displayed when I enter an unregistered e-mail adress & short password.
#    Given I am on Flip main page
    When I click Accept cookies
    When I click Contul meu
    When I insert "andrei@gmail.com" in the e-mail address field
    When I insert "a" in the password address field
    And I click the login button
    Then The "Parola trebuie sa aiba cel putin 6 caractere" message is displayed




