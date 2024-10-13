from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/"
browser.get(url)
time.sleep(2)
arama_kısmı = browser.find_element(By.XPATH, "//*[@id='search-textbox']")
arama_kısmı.send_keys("Mustafa Kemal Atatürk")
arama_butonu = browser.find_element(By.XPATH,"//*[@id='search-form']/button")
arama_butonu.click()
time.sleep(5)
i = 1
elements = browser.find_elements(By.CSS_SELECTOR, ".content")

for element in elements: 
   print("\n")
   print(str(i),":",element.text)
   i += 1

time.sleep(3)

                      
browser.close()                      



