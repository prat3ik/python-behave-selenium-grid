Feature: Amazon

    Scenario: Amazon
        Given I load the amazon website
        When I search for "Samsung" on amazon
        Then I should see "Samsung Galaxy S10 Factory Unlocked Phone with 128GB - Prism Black" in the results on amazon