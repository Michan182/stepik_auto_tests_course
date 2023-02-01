import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

num1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
result = int(num1)
def calc(result):
    return str(math.log(abs(12 * math.sin(int(result)))))
y = calc(result)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit.click()

time.sleep(5)