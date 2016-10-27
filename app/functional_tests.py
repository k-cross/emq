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

    def test_site_for_main_functionality(self):
        # Story Time:


        # A user named Jim wonders to the site hoping to buy something.

        # Because Jim is a smart man, he realizes that he needs to make an 
        # account before purchasing items.

        # After the account has been created, he logs in.

        # He adds a couple of items to his cart.

        # He decides it's time to checkout, but realizes that he wants to update the 
        # quantity of televisions that he has.

        # Then he decides to continue purchasing what's left and since he is observant,
        # he notices the subtotal, total, shipping and tax related to his county are 
        # correct.

        # He also looks at the shipping time estimate.

        # After finalizing his order, he can see the delivery being shipped and 
        # loaded in realtime.
        pass

if __name__ == '__main__':
    #display = Display(visible=0, size=(800,600))
    #display.start()

    unittest.main(warnings='ignore')
