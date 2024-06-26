from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl="https://www.saucedemo.com/"
Username="standard_user"
Password="secret_sauce"

import os

directory = 'C:\\Users\\sount\\pythonProject2\\hrmreports\\20240625'

try:
    os.makedirs(directory)
    print(f"Directory '{directory}' created successfully.")
except PermissionError as e:
    print(f"PermissionError: {e}")
except OSError as e:
    print(f"OSError: {e}")

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    global driver
    request.cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today=datetime.now()
    report_dir=Path("hrmreports",today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html=report_dir/ f"Report_{today.strftime('%Y%m%d%H%m')}.html"
    config.option.htmlpath=pytest_html
    config.option.self_contained=True

def pytest_html_report_title(report):
    report.title="HRM Test Report"
