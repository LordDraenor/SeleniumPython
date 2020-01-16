'''
Created on 5 Nov 2019

@author: Lucian
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
# import os
# 
# 
# print(os.environ['PATH'])


options = Options()
options.headless = False

driver=webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://dev.thegrommet.com")


assert "Grommet" in driver.title, "The title does not contain Grommet since it is" + driver.title
sleep(3)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div').find_elements_by_tag_name('a')[1].click()
#driver.find_element_by_xpath('//*[contains(text(),"FitKicks")]').click()
#driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div/a[2]/div/div[1]').click()
#     WebDriverWait(self.driver, 100).until(
#             lambda driver: driver.find_element_by_name(self.locator))
#     element2 = self.driver.find_element_by_name(self.locator)

    #wait = WebDriverWait(driver,10)
sleep(3)
driver.quit()
