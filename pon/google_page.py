from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'
    
    @property
    # verificar que carga correctamente con una espera 10 seg, hasta que secumpla la condicion en este caso es la presencia de q
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
    # carga del sitio verdadera
        return True

    # termino de busqueda - ubicar el campo donde estan los terninos
    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')
    
    # poder ingresar a la url
    def open(self):
        self._driver.get(self._url)
    

    #buscar los terminos
    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)
    
    # enviar el temino de busqueda
    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()
    
    # realizar la busqueda
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit
    