Feature: Google

    Scenario: Google
        Given I load the google website
        When I search for "selenium" on google
        Then I should see "https://www.selenium.dev/" in the results on google




