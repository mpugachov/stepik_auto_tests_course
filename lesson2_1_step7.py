from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #картинка с сундуком
    
    treasure = browser.find_element(By.ID, "treasure")
    
    x = treasure.get_attribute("valuex")
    y = calc(x)

   #answer
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)
    
    #checkbox
    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()
    
    #radio
    radio_element = browser.find_element(By.ID, "robotsRule")
    radio_element.click()
    
    #submit
    submit_element = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
