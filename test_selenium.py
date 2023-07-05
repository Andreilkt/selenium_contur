from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://dzen.ru/")
search_fields = driver.find_element(By.CLASS_NAME, "dzen-search-arrow-common__frame")
search_fields.send_keys("Тестирование")
search_fields.send_keys(Keys.ENTER)

#header = driver.find_element(By.TAG_NAME, "h3")
#assert header.text == "Тестирование программного обеспечения - Википедия"


sleep(5000)
driver.close()
