'''
Created on 5 Nov 2019

@author: Lucian
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


#from selenium.webdriver.common.keys import keys
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert driver.find_element_by_tag_name("h1").text=='Facebook'
#wait = WebDriverWait(driver,10)
sleep(3)
driver.quit()
#//*[@id="blueBarDOMInspector"]/div/div/div/div[1]/h1/a