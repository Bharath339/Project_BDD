from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def apply_filter(self, size):
        # Click on the filter button by size text (XS, S, M, etc.)
        locator = (By.XPATH, f"//span[text()='{size}']")
        self.click(locator)

    def get_displayed_product_count(self):
        # Return number of products currently displayed on the page
        products = self.find_elements((By.CLASS_NAME, "shelf-item"))
        return len(products)

    def add_product_by_index(self, index):
        # Add product to cart by its index in the product list
        products = self.find_elements((By.CLASS_NAME, "shelf-item"))
        if index < len(products):
            add_button = products[index].find_element(By.TAG_NAME, "button")
            add_button.click()

    def remove_first_cart_item(self):
        # Remove first product from the cart by clicking its delete button
        remove_buttons = self.find_elements((By.CLASS_NAME, "shelf-item__del"))
        if remove_buttons:
            remove_buttons[0].click()

    def get_cart_item_count(self):
        # Get count from cart badge (number of items in cart)
        cart_badge = self.driver.find_element(By.CLASS_NAME, "bag__quantity")
        if cart_badge.is_displayed():
            return int(cart_badge.text)
        else:
            return 0

    def click_checkout(self):
        # Click the checkout button
        checkout_btn = self.driver.find_element(By.CLASS_NAME, "buy-btn")
        checkout_btn.click()

    def is_checkout_modal_displayed(self):
        # Check if checkout modal/dialog is displayed
        try:
            modal = self.driver.find_element(By.CLASS_NAME, "shelf-container")
            return modal.is_displayed()
        except:
            return False
