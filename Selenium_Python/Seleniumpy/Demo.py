
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #---- It is imported for automatic download of driver 
from selenium.webdriver.chrome.service import Service #---- It is imported for automatic download of driver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver_service = Service(executable_path=ChromeDriverManager().install()) #---- Auto installs webdriver, no need to give path.

options = webdriver.ChromeOptions() 
options.add_experimental_option("detach", True) #-------- It is used in order to stop browser being closed automatically.

#--These 3 line is used in order to bypass Cloudflare Human Verification
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(service=driver_service, options=options) 

driver.set_window_position(950, 0)

driver.get("https://web.skype.com/")

driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys("abhishekmehta50@gmail.com")
driver.find_element(By.XPATH, '//input[@type="submit"]').click()
driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('9681abhi')

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()

time.sleep(2)
driver.find_element(By.ID, 'idSIButton9').click()

dr=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'Abhishek Mehta')))

dr.click()



