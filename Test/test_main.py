import time
import sys
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

# Ensure the path is correct
sys.path.append("/Users/nachetefdez/Documents/ittfWebScrapping/main")

from  page_operations import page_operations # type: ignore
from  matrix_operations import matrix_operations # type: ignore


class InputFormsCheck(unittest.TestCase):

    driver = page_operations.setUp()

    """

    def test_landingPage(self):
        
        driver = page_operations.go_to_landing_page(self.driver, "https://www.ittf.com/")

        assert "International Table Tennis Federation" in driver.title    

    def test_go_to_login(self):

        driver = page_operations.go_to_landing_page(self.driver, "https://www.ittf.com/")

        driver = page_operations.go_to_login_page(driver)

        assert "Log in" in driver.find_element(by='id', value='wsb-modal-content').text


    def test_go_to_search(self):

        driver = page_operations.go_to_landing_page(self.driver, "https://www.ittf.com/")

        driver = page_operations.go_to_login_page(driver)

        driver = page_operations.login_in_ittf(driver, "Jaime Garcia", "J&imeP#tata1")

        driver = page_operations.go_to_search_page(driver)

        assert "Players Statistics" in driver.title


    def test_insert_player_name(self):

        driver = page_operations.go_to_landing_page(self.driver, "https://www.ittf.com/")

        driver = page_operations.go_to_login_page(driver)

        driver = page_operations.login_in_ittf(driver, "Jaime Garcia", "J&imeP#tata1")

        driver = page_operations.go_to_search_page(driver)

        driver = page_operations.insert_player_name(driver, "Cifuentes", "Horacio")

        assert "Players Statistics" in driver.title


    def test_extract_links_and_years(self):

        driver = page_operations.go_to_landing_page(self.driver, "https://www.ittf.com/")

        driver = page_operations.go_to_login_page(driver)

        driver = page_operations.login_in_ittf(driver, "Jaime Garcia", "J&imeP#tata1")

        driver = page_operations.go_to_search_page(driver)

        driver = page_operations.insert_player_name(driver, "Cifuentes", "Horacio")

        data = page_operations.extract_links_and_years(driver)

        data = matrix_operations.delete_first(data)

        print(data[0][0])

        assert str(datetime.now().year) in data[0][0]

    """

    def test_scroll_years(self):

        driver = page_operations.go_to_landing_page(self.driver, "https://www.ittf.com/")

        driver = page_operations.go_to_login_page(driver)

        driver = page_operations.login_in_ittf(driver, "Jaime Garcia", "J&imeP#tata1")

        driver = page_operations.go_to_search_page(driver)

        driver = page_operations.insert_player_name(driver, "Long", "Ma")

        data = page_operations.extract_links_and_years(driver)

        data = matrix_operations.delete_first(data)

        ESTATS = page_operations.scroll_years(driver, data)

        assert "2024" in ESTATS[0][0]

    """ 
    def tearDown(self):
        self.driver.close()
    """

if __name__ == "__main__":
   unittest.main()