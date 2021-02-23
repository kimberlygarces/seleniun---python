import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SearchTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_element_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))
            
    def tearDown(self):
        self.driver.quit()

    

# detectar la existencia de items

# def test_search_text_fiels(self): #Busca por ID
#         self.driver.find_element_by_id("search_block_top")

#     def test_search_text_field_by_name(self): #Busca por  name
#         self.driver.find_element_by_name("q")

#     def test_search_text_field_class_name(self): #Busca por class name
#         self.driver.find_element_by_class_name("input-text")

#     def test_search_button_enabled(self): #Busca por class name
#         self.driver.find_element_by_class_name("button")

#     def test_count_of_promo_banner_images(self):
#         banner_list = self.driver.find_element_by_class_name("promos")
#         banners = banner_list.find_elements_by_tag_name('img') # Crea variable con los elementos del objeto IMG por tag
#         self.assertEqual(3, len(banners)) # Verifica validacion conteo de los elementos del objeto

#     def test_vip_promo(self): #Busca por XPath - Tocar dale copiar y decirle para xpath en el sitio
#         self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

#     def test_shopping_cart(self):
#         self.driver.find_element_by_css_selector("div.header-minicart span.icon")
