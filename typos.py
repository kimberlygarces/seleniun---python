import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'chromedriver.exe')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Typos").click()

    def test_find_typo(self):
        driver = self.driver
# verificar etiqueta de parrafo
        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
#extrear texto que contiene la etiqueta
        text_to_check = paragraph_to_check.text
#validar mostrando en pantalla
        print(text_to_check)
# tries numero de veces hasta encontrar el texro
        tries = 1
# deifinir si lo encontramos o no
        found = False
# texto sin error del numero del texto
        correct_text = "Sometimes you'll see a typo, other times you won't."

# cada ves que el texto sea diferente carga nuevamente el navegador
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh()
#si el texto que muestra es diferente al indicado tries aumenta en uno y found se vuel true
        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True

        self.assertEqual(found, True)

        print(f"It took {tries} tries to find the typo")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)