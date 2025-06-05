from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from Utils.Helpers import *

@given("I open the shopping website")
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
    context.driver.maximize_window()

@when('I apply "{size}" filter')
def step_apply_single_filter(context, size):
    filter_button = context.driver.find_element(By.XPATH, f"//button[contains(text(), '{size}')]")
    filter_button.click()

@then("I verify filtered results")
def step_verify_single_filter_results(context):
    item_list = context.driver.find_elements(By.CLASS_NAME, "shelf-item")
    assert len(item_list) > 0, f"No items found for the applied filter!"

@when("I apply multiple filters {size1} and {size2}")
def step_apply_multiple_filters(context, size1, size2):
    context.driver.find_element(By.XPATH, f"//button[contains(text(), '{size1}')]").click()
    context.driver.find_element(By.XPATH, f"//button[contains(text(), '{size2}')]").click()

@then("I verify multiple filters applied correctly")
def step_verify_multiple_filters(context):
    item_list = context.driver.find_elements(By.CLASS_NAME, "shelf-item")
    assert len(item_list) > 0, "No items found after applying multiple filters!"
