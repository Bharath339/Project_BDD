Feature: Update and Checkout Cart

    Scenario: Verify user can delete items from cart
        Given I open the shopping website
        When I add a few items to the cart
        Then I verify total count and price in cart
        When I remove all items from cart
        Then I verify cart count and price is reset to 0

    Scenario: Verify user can place an order
        Given I open the shopping website
        When I add a few items to the cart
        And I click "Checkout"
        Then I verify alert message displays correct total price
        And I verify cart is reset on page refresh
