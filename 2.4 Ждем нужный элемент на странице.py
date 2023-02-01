from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
book = browser.find_element(By.CSS_SELECTOR, "#book")
book.click()

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

num1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
result = int(num1)
def calc(result):
    return str(math.log(abs(12 * math.sin(int(result)))))
y = calc(result)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

button1 = browser.find_element(By.CSS_SELECTOR, "#solve")
button1.click()

time.sleep(5)