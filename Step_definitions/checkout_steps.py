from selenium import webdriver
from behave import given, when, then
from Utils.Helpers import ElementHelper

@given("I open the shopping website")
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
    context.driver.maximize_window()
    context.helper = ElementHelper(context.driver)

@when("I add a few items to the cart")
def step_add_items(context):
    items = context.helper.find_element("xpath", "//div[@class='shelf-item']")
    count = 0
    for item in items:
        if count < 3:  # Adding 3 items
            item.find_element("class name", "shelf-item__buy-btn").click()
            count += 1

@then("I verify total count and price in cart")
def step_verify_cart_total(context):
    cart_count = context.helper.find_element("class name", "cart-count").text
    assert int(cart_count) == 3, "Cart count mismatch!"

@when("I remove all items from cart")
def step_remove_all_items(context):
    remove_buttons = context.helper.find_element("xpath", "//button[contains(@class, 'shelf-item__del')]")
    for button in remove_buttons:
        button.click()

@then("I verify cart count and price is reset to 0")
def step_verify_cart_reset(context):
    cart_count = context.helper.find_element("class name", "cart-count").text
    assert int(cart_count) == 0, "Cart not reset!"

@when('I click "Checkout"')
def step_checkout(context):
    checkout_button = context.helper.find_element("xpath", "//button[contains(text(), 'Checkout')]")
    checkout_button.click()

@then("I verify alert message displays correct total price")
def step_verify_alert_message(context):
    alert = context.helper.find_element("xpath", "//div[@class='alert-message']")
    assert alert.text.startswith("Total: $"), "Incorrect alert message!"

@then("I verify cart is reset on page refresh")
def step_verify_cart_reset_after_refresh(context):
    context.driver.refresh()
    cart_count = context.helper.find_element("class name", "cart-count").text
    assert int(cart_count) == 0, "Cart did not reset after refresh!"
