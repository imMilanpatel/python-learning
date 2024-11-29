from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ie_options = webdriver.IeOptions()
ie_options.attach_to_edge_chrome = True
ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

driver = webdriver.Ie(options=ie_options)

driver.get("http://www.bing.com")
elem = driver.find_element(By.ID, 'sb_form_q')
elem.send_keys('WebDriver' + Keys.RETURN)

driver.quit()

#Imported from Microsoft Official Page