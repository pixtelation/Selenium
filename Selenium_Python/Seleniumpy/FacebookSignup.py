
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  #---- It is imported for automatic download of driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

'''
driver_service = Service(executable_path="C:/selenium-java-4.1.0/chromedriver.exe") #Path is required for webdriver
'''

'''
#These below 2 codes are written to run script in already opened browser again & again.
#To follow tutorial on this visit - https://www.youtube.com/watch?v=Zrx8FSEo9lk

opt=Options()
opt.add_experimental_option("debuggerAddress", "localhost:4848")
'''

driver_service = Service(executable_path=ChromeDriverManager().install()) #---- Auto installs webdriver, no need to give path.

# These below 2 codes are written in order to stop browser being closed automatically.
options = webdriver.ChromeOptions() 
options.add_experimental_option("detach", True)

# options=options--- Used to stop browser being closed automatically
# chrome_options=opt--- Used to run script in same opened browser again
driver = webdriver.Chrome(service=driver_service, options=options) 



driver.get("https://www.facebook.com/")
driver.implicitly_wait(5) #------ Implicit Wait is used to make the driver keep searching element for specific period of time.  
                              #-- If the element is not found after specified time then it throws exception                                                                                                
driver.find_element(By.LINK_TEXT, 'Create New Account').click()
driver.find_element(By.NAME, 'firstname').send_keys('Abhishek')
driver.find_element(By.NAME, 'lastname').send_keys('Mehta')
driver.find_element(By.XPATH, '//input[@name="reg_email__"]').send_keys('testdemo@yopmail.com')
driver.find_element(By.XPATH, '//input[@name="reg_email_confirmation__"]').send_keys('testdemo@yopmail.com')
driver.find_element(By.XPATH, '//*[@id="password_step_input"]').send_keys('22720546')

day = Select(driver.find_element(By.ID, 'day'))
day.select_by_index(22)

month = Select(driver.find_element(By.ID, 'month'))
month.select_by_index(9)

year = Select(driver.find_element(By.ID, 'year'))
year.select_by_value('1994')

driver.find_element(By.XPATH, '//input[@value="2"]').click()
driver.find_element(By.XPATH, '//button[@name="websubmit"]').click()








