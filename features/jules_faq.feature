Feature: Jules FAQ page
  Background:
    Given I want to read the FAQ

    @FAQ
    Scenario: Read the FAQ
      When I click on FAQ
      Then I am on the FAQ Page