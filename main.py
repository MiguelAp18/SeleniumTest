from selenium import webdriver
import time 

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://es.investing.com/crypto/bitcoin")

time.sleep(5)

precioBTC = driver.find_element_by_xpath('//*[@id="last_last"]')

print(precioBTC.text)

driver.quit()