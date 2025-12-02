import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TestLogin(unittest.TestCase):
    """
    Selenium tests for yourlearningpal.com login page.

    Scenarios:
    - Successful login  (username: test1, password: Test12456)
    - Failed login      (username: test1, password: test1234)
    """

    def setUp(self):
        """Open browser and navigate to login page."""
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yourlearningpal.com/login")
        time.sleep(1)

    def tearDown(self):
        """Close browser after short pause."""
        time.sleep(1)
        self.driver.quit()

    # ---------------- helper ----------------

    def do_login(self, username: str, password: str):
        """Enter credentials, show password, click Login."""
        driver = self.driver

        user_input = driver.find_element(By.ID, "txtUser")
        pass_input = driver.find_element(By.ID, "txtPassword")

        user_input.clear()
        pass_input.clear()

        user_input.send_keys(username)
        time.sleep(0.5)

        pass_input.send_keys(password)
        time.sleep(0.5)

        # Clicking the "show password" icon (optional)
        try:
            eye = driver.find_element(By.CSS_SELECTOR, "i[aria-label='Show password']")
            eye.click()
            time.sleep(1)
        except NoSuchElementException:
            pass  # Icon not found, continue without showing password

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # ---------------- tests ----------------

    def test_success_login(self):
        """Correct credentials should redirect to CourseSelection."""
        self.do_login("test1", "Test12456")
        time.sleep(2)
        self.assertIn("CourseSelection", self.driver.current_url)

    def test_failed_login(self):
        """Wrong password should keep user on login page."""
        self.do_login("test1", "test1234")
        time.sleep(2)
        self.assertIn("login", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
