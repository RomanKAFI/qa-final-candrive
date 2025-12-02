This project contains Python unit tests and Selenium UI tests.

Included files:

can_drive.py – simple function that checks if a person can drive based on age

test_can_drive.py – unit tests for can_drive

test_login_selenium.py – Selenium tests for the login page on https://www.yourlearningpal.com/login

Requirements:
Python 3.10 or higher, Google Chrome, and the following packages:

pip install selenium webdriver-manager


How to run unit tests:

python -m unittest test_can_drive.py


How to run Selenium login tests:

python -m unittest test_login_selenium.py


Browser slow-motion mode can be enabled in test_login_selenium.py:

DEBUG_SLOW = True
DEBUG_DELAY = 1.0


Set DEBUG_SLOW = False to run the tests at full speed.