from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

   #answer
    answer_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_element.send_keys(y)
    
    #checkbox
    checkbox_element = browser.find_element(By.CSS_SELECTOR, ".form-check-custom .form-check-label")
    checkbox_element.click()
    
    #radio
    radio_element = browser.find_element(By.CSS_SELECTOR, ".form-radio-custom .form-check-label")
    radio_element.click()
    
    #submit
    submit_element = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
