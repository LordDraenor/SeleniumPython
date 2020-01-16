'''
Created on 5 Nov 2019

@author: Lucian
'''
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep


#from selenium.webdriver.common.keys import keys\
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get("https://dev.thegrommet.com")

assert "Grimmet" in driver.title, "The title does not contain Grimmet since it is" + driver.title

#wait = WebDriverWait(driver,10)
sleep(3)
driver.quit()
#//*[@id="blueBarDOMInspector"]/div/div/div/div[1]/h1/a