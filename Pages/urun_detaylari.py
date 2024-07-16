from pathlib import Path
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest
S="https://www.tesla.com/tr_tr/models" # Model S sayfa url
E="https://www.tesla.com/tr_tr/model3" # Model 3 sayfa url
X="https://www.tesla.com/tr_tr/modelx" # Model X sayfa url
Y="https://www.tesla.com/tr_tr/modely" # Model Y sayfa url 
CYBER="https://www.tesla.com/tr_tr/cybertruck"    # Model CyberTruck url
Roadster="https://www.tesla.com/tr_tr/roadster"   # Model Roadster url
Powerwall="https://www.tesla.com/tr_tr/powerwall" # Ürün PowerWall url
MegaPack="https://www.tesla.com/tr_tr/megapack"   # Ürün MegaPack url
@pytest.mark.usefixtures("setup")
class urun_detaylari_:
    def __init__(self,driver):
        self.driver=driver
        
        
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
    def modelS_page_doğrulama_url(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__subcopy-desktop")))
        Url=self.driver.current_url

        print("Sayfa URL'i:"+Url)
        assert S==Url  #Url ile sayfa doğrulama
    def modelS_page_ekran_görüntüsü_al(self):
        self.driver.save_screenshot(f"{self.folderPath}/test-Model-S.png")
    def model3_page_doğrulama_url(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
        Url=self.driver.current_url
        print("Sayfa URL'i:"+Url)
        assert E==Url #Url ile sayfa doğrulama
    def model3_page_ekran_görüntüsü_al(self):
        self.driver.save_screenshot(f"{self.folderPath}/test-Model-3.png")
    def modelX_page_doğrulama_url(self):
        Url=self.driver.current_url
        print("Sayfa URL'i:"+Url)
        assert X==Url   #Url ile sayfa doğrulama
    def modelX_page_ekran_görüntüsü_al(self):
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Model-X.png")
    def modelY_page_doğrulama_url(self):
        Url=self.driver.current_url
        print("Sayfa URL'i:"+Url)
        assert Y==Url   #Url ile sayfa doğrulama  
    def modelY_page_ekran_görüntüsü(self):
        time.sleep(3)
        self.driver.save_screenshot(f"{self.folderPath}/test-Model-Y.png")
    def model_CyberTruck_page_doğrulama_url(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".dx-hero-content svg")))
        time.sleep(1)
        Url=self.driver.current_url
        print("Sayfa URL'i:"+Url)
        assert CYBER==Url #Url ile sayfa doğrulama
    def model_CyberTruck_ekran_görüntüsü_al(self):
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Model-CyberTruck.png")    
    def model_Roadster_page_doğrulama_url(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
        time.sleep(1)
        Url=self.driver.current_url
        print("Sayfa URL'i:"+Url)
        assert Roadster==Url #Url ile sayfa doğrulama
    def model_Roadster_ekran_görüntüsü_al(self):
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Model-Roadster.png")
    def urun_powerwall_page_doğrulama_url(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
        time.sleep(1)
        Url=self.driver.current_url
        print("Sayfa URL'i:"+Url)
        assert Powerwall==Url #Url ile sayfa doğrulama
    def Urun_Powerwall_ekran_görüntüsü_al(self):
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Page-PowerWall.png")    
    def Urun_MegaPack_page_doğrulama_url(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
        time.sleep(1)
        Url=self.driver.current_url
        print("Sayfa URL'i:"+Url)
        assert MegaPack==Url #Url ile sayfa doğrulama
    def Urun_MegaPack_ekran_görüntüsü_al(self):
        time.sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-Page-Megapack.png")



    