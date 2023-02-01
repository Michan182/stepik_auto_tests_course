from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = int(num1)
    def calc(result):
        return str(math.log(abs(12 * math.sin(int(result)))))
    y=calc(result)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    option3.click()
finally:
    time.sleep(10)
    browser.quit()
