import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Slow-motion settings to visually watch the tests in the browser
DEBUG_SLOW = True        # False = no extra delays
DEBUG_DELAY = 1.0        # default delay in seconds


class TestLogin(unittest.TestCase):
    """
    Selenium tests for login on yourlearningpal.com:
    - valid login
    - invalid login (wrong password)
    """

    def slow(self, seconds: float = DEBUG_DELAY) -> None:
        """
        Optional pause to visually follow what happens in the browser.
        Turn off via DEBUG_SLOW.
        """
        if DEBUG_SLOW and seconds > 0:
            time.sleep(seconds)

    def setUp(self):
        """Start browser and open the login page."""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-search-engine-choice-screen")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options,
        )
        self.wait = WebDriverWait(self.driver, 15)

        self.driver.get("https://www.yourlearningpal.com/login")
        self.slow(1)  # quick look at the login page

    def tearDown(self):
        """Short pause to see final state, then close browser."""
        self.slow(1)
        self.driver.quit()

    # -------- helper --------

    def do_login(self, username_value: str, password_value: str) -> None:
        """Fill username/password, show password, click Login."""
        driver = self.driver

        # username / password fields
        username = self.wait.until(
            EC.visibility_of_element_located((By.ID, "txtUser"))
        )
        password = driver.find_element(By.ID, "txtPassword")

        username.clear()
        password.clear()

        username.send_keys(username_value)
        self.slow(0.3)

        password.send_keys(password_value)
        self.slow(0.5)

        # click eye icon so password is visible (no dots)
        try:
            show_pwd_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "i[aria-label='Show password']")
                )
            )
            show_pwd_btn.click()
            # small pause to see plain text password
            self.slow(1.0)
        except TimeoutException:
            # if eye icon is not found – continue test anyway
            pass

        # Login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

    # -------- tests --------

    def test_success_login(self):
        """
        Valid login:
        - use correct credentials
        - expect redirect to CourseSelection page
        """
        self.do_login("test1", "Test12456")

        # wait for redirect after successful login
        self.wait.until(EC.url_contains("CourseSelection"))
        self.slow(1)  # see the course page

        current_url = self.driver.current_url
        self.assertIn("CourseSelection", current_url)

    def test_failed_login_wrong_password(self):
        """
        Invalid login:
        - correct username + wrong password
        - expect to stay on login page
        """
        self.do_login("test1", "test1234")
        self.slow(1.5)  # time to show error

        current_url = self.driver.current_url
        self.assertIn("login", current_url)


if __name__ == "__main__":
    # run with: python -m unittest test_login_selenium.py
    unittest.main()
