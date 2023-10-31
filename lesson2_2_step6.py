from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = int(browser.find_element(By.ID, "input_value").text)
    y = math.log(abs(12*math.sin(x)))
    
   #answer
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)
    
    submit_element = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_element)
    
    #checkbox
    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()
    
    #radio
    radio_element = browser.find_element(By.ID, "robotsRule")
    radio_element.click()
    
    #submit
    submit_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
