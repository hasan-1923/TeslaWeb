from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pathlib import Path
from datetime import date, datetime

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.tesla.com/tr_tr")
    driver.set_window_size(1552, 832)
    request.cls.driver = driver
    yield
    driver.quit()
def pytest_html_report_title(report):
    report.title ="Test Otomasyon Raporu "
def pytest_configure(config):
    bugun =datetime.now()
    rapor_klasoru=Path("raporlar",bugun.strftime("%y-%m-%d"))
    rapor_klasoru.mkdir(parents=True,exist_ok=True)
    rapor=rapor_klasoru/f"rapor{bugun.strftime('%H-%M')}.html"
    config.option.htmlpath=rapor
    config.option.self_contained_html=True
        