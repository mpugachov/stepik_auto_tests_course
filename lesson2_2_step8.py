from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    firstname = "name"
    lastname = "last_name"
    email = "somebody@email.com"
 
    browser.find_element(By.NAME, "firstname").send_keys(firstname)
    browser.find_element(By.NAME, "lastname").send_keys(lastname)
    browser.find_element(By.NAME, "email").send_keys(email)
    
    #file
    element_browse = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'flie2_2_step8.txt')           # добавляем к этому пути имя файла 
    element_browse.send_keys(file_path)    
     
     #submit
    submit_element = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
