import unittest
from pyunitreport import HTMLTestRunner
from time import sleep
from selenium import webdriver

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver")
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver
#seleccionar pais
        country = driver.find_element_by_id('CO')
        country.click()
#inspecionar barra de busqueda 
        search_field = driver.find_element_by_name('as_word')
#darle click en la barra de busqueda
        search_field.click()
#limpiar la barra de busqueda
        search_field.clear()
#escribir termino de busqueda
        search_field.send_keys('playstation 4')
#buscar summit
        search_field.submit()
        sleep(3)
# filtro de ubicacion = texto parcial del enlace
        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()
        sleep(3)
# filtro de condicion 
        condition = driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)
# ordenar publicaciones 
        order_menu = driver.find_element_by_class_name('ui-dropdown__link')
        order_menu.click()
# en este caso seleccionar la de mayor precio
        higher_price = driver.find_element_by_css_selector('#inner-main > aside > section.view-options > dl > div > div > div > div > ul > li:nth-child(3) > a')
        higher_price.click()
        sleep(3)
# crear dos listas donde se almacena la informacion
        articles = []
        prices = []
# extraer la informacion de 5 elementos
        for i in range(5):
            # optenemos xpath de nombre del articulo
            article_name = driver.find_element_by_xpath(f'/html/body/main/div[2]/div/section/ol/li[{i + 1}]/div/div[2]/div/h2/a/span').text
            articles.append(article_name)
# optener por el precio
            article_price = driver.find_element_by_xpath(f'/html/body/main/div[2]/div/section/ol/li[{i + 1}]/div/div[2]/div/div[1]/div/span[2]').text
            prices.append(article_price)
        
        print(articles, prices)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'ml-report'))