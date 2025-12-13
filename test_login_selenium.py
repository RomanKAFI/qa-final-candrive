import unittest 
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yourlearningpal.com/login")
        time.sleep(2)
                   
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def do_login(self, username, password: str):
        driver = self.driver

        user_input = driver.find_element(By.ID, "txtUser")
        pass_input = driver.find_element(By.ID, "txtPassword")

        user_input.clear()
        pass_input.clear()

        user_input.send_keys(username)
        time.sleep(2)

        pass_input.send_keys(password)
        time.sleep(2)

        eye = driver.find_element(By.CSS_SELECTOR, "i[aria-label='Show password']")
        eye.click()
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_successful_login(self):
        self.do_login("test1", "Test12456")
        time.sleep(2)
        self.assertIn("CourseSelection", self.driver.current_url)

    def test_failed_login(self):
        self.do_login("test1", "test1234")
        time.sleep(2)
        self.assertIn("login", self.driver.current_url)




if __name__ =="__main__":
    unittest.main()
