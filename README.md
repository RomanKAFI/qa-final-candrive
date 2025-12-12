Final Project – CanDrive Unit Tests & Selenium Login Test

This repository contains the solution for Part 1 of the final:

Unit tests for the can_drive(age) function (Python version).

Selenium UI tests for the login page at letsusedata.com
(one successful login and one failed login).

Files

can_drive.py – implementation of can_drive(age) (returns True if age ≥ 16).

test_can_drive.py – unit tests for can_drive(age) using Python unittest.

test_login_selenium.py – Selenium tests for:

successful login: test1 / Test12456

failed login: test1 / test1234

.gitignore – ignores .venv/, __pycache__/ and other non-essential files.

Requirements

Python 3 – to run the scripts.

Google Chrome – Selenium opens this browser to perform UI tests.

Selenium library – allows Python to control the browser.

Install Selenium:

pip install selenium

Optional: Virtual Environment

Used to isolate project dependencies so the project runs the same on any machine.

python -m venv .venv
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows

How to Run the Tests
1. Run unit tests (CanDrive)
python3 test_can_drive.py

2. Run Selenium login tests
python3 test_login_selenium.py


Selenium will open Chrome, type the credentials, click the “show password” icon, and verify both successful and failed login scenarios.
