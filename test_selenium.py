from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.ru")
driver.close()
