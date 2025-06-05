from selenium import webdriver
from behave import given, when, then
from Utils.Helpers import ElementHelper

@given("I open the shopping website")
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
    context.driver.maximize_window()
    context.helper = ElementHelper(context.driver)

@when("I add 4 random free shipping items to cart")
def step_add_free_shipping_items(context):
    items = context.helper.find_element("xpath", "//div[@class='shelf-item']")
    count = 0
    for item in items:
        if "Free shipping" in item.text and count < 4:
            item.find_element("class name", "shelf-item__buy-btn").click()
            count += 1

@when("I add 1 item without free shipping to cart")
def step_add_non_free_shipping_item(context):
    items = context.helper.find_element("xpath", "//div[@class='shelf-item']")
    for item in items:
        if "Free shipping" not in item.text:
            item.find_element("class name", "shelf-item__buy-btn").click()
            break

@then("I verify items are listed in cart in order with correct price")
def step_verify_cart_order(context):
    cart_items = context.helper.find_element("xpath", "//div[@class='float-cart__shelf-item']")
    assert len(cart_items) == 5, "Items are not added correctly!"

@when("I add a same item multiple times using 'Add to cart' button")
def step_add_same_item_multiple_times(context):
    item = context.helper.find_element("xpath", "//div[@class='shelf-item']")
    item.find_element("class name", "shelf-item__buy-btn").click()
    item.find_element("class name", "shelf-item__buy-btn").click()

@then("I verify item count and price are updated in cart")
def step_verify_item_count_price(context):
    cart_count = context.helper.find_element("class name", "cart-count").text
    assert int(cart_count) > 1, "Item count is not updated!"

@when("I add an existing item using '+' button")
def step_increment_existing_item(context):
    plus_button = context.helper.find_element("class name", "cart-item__quantity-plus")
    plus_button.click()

@then("I verify item count and price are updated accordingly")
def step_verify_cart_update(context):
    cart_count = context.helper.find_element("class name", "cart-count").text
    assert int(cart_count) > 2, "Item count did not update correctly!"
