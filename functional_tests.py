from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#import time
#time.sleep(10)

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about...
        self.browser.get('http://localhost:8000')
        # she notices the page title...
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # she is invited to enter...
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
# She types "Buy peacock feathers..."
        inputbox.send_keys('Buy peacock feathers')
# When she hits enter...
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
# There is still a text box... she enters "Use peacock feathers..."
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
# The page updates again...
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])
# Edith wonders... unique URL ...
        self.fail('Finish the test!')
# She visits that URL ...

# Satisfied, she...

if __name__ == '__main__':
    unittest.main(warnings='ignore')
