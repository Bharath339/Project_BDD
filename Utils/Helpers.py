from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionHelper:
    def _init_(self, driver):
        self.driver = driver

    def find_element(self, locator_type, locator, timeout=10):
        """Find a single element with explicit wait."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator))
            )
        except Exception as e:
            print(f"Error: Element {locator} not found! {str(e)}")
            return None

    def find_elements(self, locator_type, locator, timeout=10):
        """Find multiple elements with explicit wait."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((locator_type, locator))
            )
        except Exception as e:
            print(f"Error: Elements {locator} not found! {str(e)}")
            return []

    def click_element(self, locator_type, locator, timeout=10):
        """Click an element with explicit wait."""
        element = self.find_element(locator_type, locator, timeout)
        if element:
            element.click()
        else:
            print(f"Error: Cannot click {locator}, element not found!")

    def enter_text(self, locator_type, locator, text, timeout=10):
        """Enter text into an element."""
        element = self.find_element(locator_type, locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f"Error: Cannot enter text in {locator}, element not found!")