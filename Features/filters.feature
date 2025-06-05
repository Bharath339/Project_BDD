Feature: Filter Validations
    Scenario: Verify single filter selection
        Given I open the shopping website
        When I apply "S" filter
        Then I verify filtered results

    Scenario: Verify multiple filters applied correctly
        Given I open the shopping website
        When I apply multiple filters "S" and "M"
        Then I verify multiple filters applied correctly
