from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    #нажимаем кнопку "i want..."
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    
    #переключаемся на новое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    #капча
    x = int(browser.find_element(By.ID, "input_value").text)
    y = math.log(abs(12*math.sin(x)))
    
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)
    
    submit_element = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
