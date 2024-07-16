import getpass
from datetime import datetime
from pathlib import Path
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest

@pytest.fixture(scope="class")
def setup(request, environment,browser ):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        
    elif browser == "safari": #bu projede safari kullanilmadi, ornek icin konuldu
        service = service("./drivers/safari")
        driver = webdriver.Chrome(service=service)
        
    else:
        print("heeey dogru durust bir tarayici gir")
    if environment is None:
        print("environment girmeyi unutmayin..")
    else:
        if environment == "dev":
            base_url = "https://dev-www.tesla.com/tr_tr"
            driver.get(base_url)
        elif environment == "qa":
            base_url = "https://qa-www.tesla.com/tr_tr"
            driver.get(base_url)
        elif environment == "test":
            base_url = "https://test-www.tesla.com/tr_tr"
            driver.get(base_url)
        elif environment == "prod":
            base_url = "https://www.tesla.com/tr_tr"
            driver.get(base_url)
        else:
            print("Environment degeri hatali. Lutfen parametreyi kontol edin")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.baseurl = base_url
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def environment(request):
    return request.config.getoption("--env")


def pytest_html_report_title(report):
    report.title = "Test Otomasyon Raporu"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):

    bugun = datetime.now()
    rapor_klasoru = Path('raporlar', bugun.strftime('%Y-%m-%d'))
    rapor_klasoru.mkdir(parents=True, exist_ok=True)
    rapor = rapor_klasoru / f"rapor_{bugun.strftime('%H-%M')}.html"
    config.option.htmlpath = rapor
    config.option.self_contained_html = True

@pytest.hookimpl(tryfirst=True)
def configure_html_report_env(request, environment, browser):
    request.config._metadata.update(
        {
            'user': getpass.getuser(),
            'environment': environment,
            'browser': browser
        }
    )
        