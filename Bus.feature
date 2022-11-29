Feature: Bus

  Background: common steps
    Given Open the chrome browser
    When  Enter the URL

  Scenario: Bus Module
    Given Click on "From" text field
    When Enter the cityName in FromSearch
    Then Click on "To" text field and enter cityname
    Then Click on "DateOfJourney"
    Then Click on "SearchButton"
    And Select the seat
    And select the one boarding point
    And select the one dropping point
    And Click on Continue Button
    And Enter the valid passenger LoginNo in the text field
    Then Enter the valid passenger Email in the text field
    And Enter the valid passenger Mobile number in the text field
    And Enter the valid passenger name in the text field
    And Enter the valid passenger Age in the text field
    Then Click on Agree & Terms checkbox