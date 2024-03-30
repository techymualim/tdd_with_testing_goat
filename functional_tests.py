import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_to_do_list(self):
        #Edith has heard about a new cool web app for to do list
        #She opens browser and types and goes there 
        self.browser.get("http://localhost:8000")

        #She notices that on title or header To Do List is mentioned
        self.assertIn("To-Do",self.browser.title)

        #She is then invited to add to do Item

        self.fail("Complete the freaking test")


if  __name__ == "__main__":
    unittest.main()