from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()
        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)).is_displayed()
        except TimeoutException:
            return False

    def find_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def scroll_into_view(self, by_locator):
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
