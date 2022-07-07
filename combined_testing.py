import requests
import db_connector
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    user_id = 1
    user_name = "afik"

    requests.post(url=f"http://localhost:5000/users/{int(user_id)}", json={"user_name": user_name})
    requests.get(url=f"http://localhost:5000/users/{int(user_id)}")
    check_db = db_connector.get_username(int(user_id))
    print(f"user id: {user_id} is bound in DB to {check_db}")
    driver = webdriver.Chrome(executable_path='/Users/afik.navaro/Documents/chromedriver')

    driver.implicitly_wait(5)
    driver.get(f"http://localhost:5001/users/get_user_data/{user_id}")
    locator = driver.find_element(by=By.ID, value="user").text
    if locator == user_name:
        print("Correct, user posted in REST API is bound to the id entered")
    else:
        print("Wrong, the user name entered is not bound to the id entered")
except Exception:
    raise Exception("failed test")
