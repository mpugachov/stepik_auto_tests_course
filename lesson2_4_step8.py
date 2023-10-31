from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    #ждем, пока цена уменьшится до 100$ и жмем "Book"
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
    browser.find_element(By.ID, "book").click()
    
    # #капча
    x = int(browser.find_element(By.ID, "input_value").text)
    y = math.log(abs(12*math.sin(x)))
    
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)
    
    submit_element = browser.find_element(By.ID, "solve")
    submit_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
