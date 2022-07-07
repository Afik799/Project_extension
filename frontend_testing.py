from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/afik.navaro/Documents/chromedriver')

driver.implicitly_wait(5)
driver.get("http://localhost:5001/users/get_user_data/1")
Web_element = driver.find_element(by=By.XPATH, value="//body/h1")
locator = driver.find_element(by=By.ID, value="user").text
print(locator)

driver.close()
