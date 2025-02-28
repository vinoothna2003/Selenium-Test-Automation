# Selenium Test Automation 

##  About This Project
This repository contains an automated login test using **Selenium & PyTest**.  
It automates the login process for [SauceDemo](https://www.saucedemo.com/) and generates an HTML test report.

##  Prerequisites 
### 1. Install Python (If Not Installed)
- Download & install **Python 3.10+** 
- Check installation:  in bash
  python --version

### 2. Install Google Chrome & ChromeDriver
- **Download ChromeDriver** matching your Chrome version  
- Move `chromedriver.exe` to a known location (Example: `C:\chromedriver\`)  
- Add it to the **system PATH** (optional for automatic detection)

## Steps to Run the Test 
### 1. Install Required Python Packages
in bash
pip install pytest selenium pytest-html

### 2. Run the Test Case
in bash
pytest test_login.py --html=report.html --self-contained-html

### 3. View the Test Report
- Open "report.html" in your browser to see the test results.

## Project Details 
- Uses **PyTest** for structured test cases  
- Automates login for **https://www.saucedemo.com/**  
- Generates an **HTML report** with test results  
- Uses **Selenium WebDriver** to interact with the website  
