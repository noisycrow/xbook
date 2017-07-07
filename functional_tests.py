from selenium import webdriver
import unittest

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

        self.fail('Finish the test!')

# she is invited to enter...

# She types "Buy peacock feathers..."

# When she hits enter...

# There is still a text box... she enters "Use peacock feathers..."

# The page updates again...

# Edith wonders... unique URL ...

# She visits that URL ...

# Satisfied, she...

if __name__ == '__main__':
    unittest.main(warnings='ignore')
