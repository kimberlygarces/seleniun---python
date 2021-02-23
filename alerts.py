import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_renoval_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
# Buscar elemento enviando la simulacion del text

        search_field.send_keys('Tee')
        search_field.submit()

#encuentro el elemento por el texto del enlace

        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

#atender alert
        alert = driver.switch_to.alert
#verificar si el texto del alert es la que queremos
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert.text)
        driver.implicitly_wait(30)
#aceptar alerta
        alert.accept()

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)