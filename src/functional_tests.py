from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
import unittest
import time


class ShoppingCartTest(unittest.TestCase):
    def setup(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) 

    def tearDown(self):
        self.browser.quit()

    def test_shopping_cart_for_problems(self):
        pass

if __name__ == '__main__':
    #display = Display(visible=0, size=(800,600))
    #display.start()

    unittest.main(warnings='ignore')
