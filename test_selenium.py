from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.rambler.ru/")
search_fields = driver.find_element(By.NAME, "query")
search_fields.send_keys("Тестирование")
search_fields.send_keys(Keys.ENTER)

header = driver.find_element(By.TAG_NAME, "h3")
assert header.text == "Тестирование программного обеспечения - Википедия"


sleep(10)
driver.close()
