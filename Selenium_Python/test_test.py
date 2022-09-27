# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
    
  def test_test(self):
    # Test name: test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://www.abhiinc.c1.biz/")
    # 2 | setWindowSize | 974x1032 | 
    self.driver.set_window_size(974, 1032)
    # 3 | click | css=.caret | 
    self.driver.find_element(By.CSS_SELECTOR, ".caret").click()
    # 4 | click | linkText=Sign In | 
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    # 5 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 6 | type | name=username | admin
    self.driver.find_element(By.NAME, "username").send_keys("admin")
    # 7 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 8 | type | id=password | 22720546
    self.driver.find_element(By.ID, "password").send_keys("22720546")
    # 9 | click | id=togglePasswordField | 
    self.driver.find_element(By.ID, "togglePasswordField").click()
    # 10 | click | name=submit | 
    self.driver.find_element(By.NAME, "submit").click()
  