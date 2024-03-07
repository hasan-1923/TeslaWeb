import pytest
import time

from Pages.anasayfa import Anasayfa
from Pages.urun_detaylari import urun_detaylari_


@pytest.mark.usefixtures("setup")
class TestÜrünDetaylari:
    def test_Models_test_(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)

        anasayfa.ModelS_click()
        time.sleep(1)
        urun_detaylari.modelS_page_doğrulama_url()
        time.sleep(1)
        urun_detaylari.modelS_page_ekran_görüntüsü_al()
    def test_Model3_test_(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)

        anasayfa.Models3_click()
        time.sleep(1)
        urun_detaylari.model3_page_doğrulama_url()
        
        urun_detaylari.model3_page_ekran_görüntüsü_al()
    def test_ModelX_test(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)

        anasayfa.ModelX_click()
        urun_detaylari.modelX_page_doğrulama_url()
        time.sleep(1)
        urun_detaylari.modelX_page_ekran_görüntüsü_al()
    def test_ModelY_test(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)

        anasayfa.ModelY_click()
        urun_detaylari.modelY_page_doğrulama_url()
        urun_detaylari.modelY_page_ekran_görüntüsü()
    def test_ModelCyberTruck_test(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)
        
        anasayfa.ModelCyberTruck_click()
        urun_detaylari.model_CyberTruck_page_doğrulama_url()
        urun_detaylari.model_CyberTruck_ekran_görüntüsü_al()
    def test_ModelRoaster_test(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)
        
        anasayfa.ModelRoadster_click()
        urun_detaylari.model_Roadster_page_doğrulama_url()
        urun_detaylari.model_Roadster_ekran_görüntüsü_al()
    def test_powerwall_test(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)

        anasayfa.Urun_Powerwall_click()
        urun_detaylari.urun_powerwall_page_doğrulama_url()
        urun_detaylari.Urun_Powerwall_ekran_görüntüsü_al()
    def test_MegaPack_test(self):
        anasayfa=Anasayfa(self.driver)
        urun_detaylari=urun_detaylari_(self.driver)

        anasayfa.Urun_MegaPack_click()
        urun_detaylari.Urun_MegaPack_page_doğrulama_url()
        urun_detaylari.Urun_MegaPack_ekran_görüntüsü_al()


        


       

        




