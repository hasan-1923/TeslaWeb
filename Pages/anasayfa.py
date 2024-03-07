from pathlib import Path
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

S="Model S"
E="Öğren"
X="Model X"



class Anasayfa:
    def __init__(self,driver):
        self.driver = driver
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
    def ModelS_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Model S")))
        self.driver.find_element(By.LINK_TEXT,S).click()
    def Models3_click(self):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, E).click()
    def ModelX_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
        time.sleep(1)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Model X")))
        self.driver.find_element(By.LINK_TEXT, X).click()
    def ModelY_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text")))
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(2) .tds-link:nth-child(1)")))
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(2) .tds-link:nth-child(1)").click()
    def ModelCyberTruck_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(3) .tds-link")))
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(3) .tds-link").click()
    def ModelRoadster_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Roadster")))
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Roadster").click()
    def Urun_Powerwall_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--energy > .tds-site-nav-item-text").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".dx-mega-menu-products--count-2 .dx-mega-menu-product:nth-child(1) img")))
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".dx-mega-menu-products--count-2 .dx-mega-menu-product:nth-child(1) img").click()
    def Urun_MegaPack_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--energy > .tds-site-nav-item-text").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".dx-mega-menu-products--count-2 .dx-mega-menu-product:nth-child(2) img")))
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".dx-mega-menu-products--count-2 .dx-mega-menu-product:nth-child(2) img").click()