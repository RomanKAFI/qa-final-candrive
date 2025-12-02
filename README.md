QA Automation Project (Unit Tests + Selenium)

This project includes:

Unit tests for the can_drive(age) function

Selenium tests for the login page at:
https://www.yourlearningpal.com/login

Requirements

Python 3

Google Chrome

pip install selenium

(optional) virtual environment:

python -m venv .venv
source .venv/bin/activate     # macOS/Linux
.\.venv\Scripts\activate      # Windows

▶ How to Run Unit Tests
python -m unittest test_can_drive.py

▶ How to Run Selenium Tests
python -m unittest test_login_selenium.py


Selenium will:

open Chrome

enter login and password

click the “show password” icon (if available)

test successful and failed login scenarios

Notes

Chrome is required because WebDriver uses it by default.

.venv and __pycache__ are ignored through .gitignore.

Add your demo appointment date/time inside test file comments (as required).