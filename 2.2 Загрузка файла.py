import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("EGOR")

    surname = browser.find_element(By.NAME, "lastname")
    surname.send_keys("SUPERIOR")

    e_mail = browser.find_element(By.NAME, "email")
    e_mail.send_keys("super@yahoo.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit.click()
    
finally:
    time.sleep(5)
    browser.quit()
