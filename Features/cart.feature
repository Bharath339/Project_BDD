Feature: Cart validations

  Scenario: Verify user can add a single product to the cart
    Given the user is on the homepage
    When the user adds the first product to the cart
    Then the cart should show 1 item

  Scenario: Verify user can add multiple products to the cart
    Given the user is on the homepage
    When the user adds the first product to the cart
    And the user adds the second product to the cart
    Then the cart should show 2 items

  Scenario: Verify user can remove a product from the cart
    Given the user has added 2 products to the cart
    When the user removes one product from the cart
    Then the cart should show 1 item
