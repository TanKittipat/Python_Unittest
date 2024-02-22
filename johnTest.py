from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import unittest

class TestInput1(unittest.TestCase):
    def test_input1(self):
        service = Service('D:\\webdriver\\chromedriver-win64\\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canonc")
        age.send_keys("2")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("result.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)
        
        driver.close()

if __name__ == "__main__":
    unittest.main()
