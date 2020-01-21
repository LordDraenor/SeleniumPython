'''
@author: Lucian
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


#Set headless, window size (It's 800X600 by default) and an implicit wait - set up proper wait later
options = Options()
options.headless = True
options.add_argument("--window-size=1600,1200")
driver=webdriver.Chrome(options=options)
driver.implicitly_wait(10)

#Go to the main site and check that you're there
driver.get("https://dev.thegrommet.com")
assert "Grommet" in driver.title, "The title does not contain Grommet since it is" + driver.title
#Click the second item in the recent discoveries group
driver.find_element_by_xpath('//div[@class="tile-container-3 tile-container-2-mobile"]').find_elements_by_tag_name('a')[1].click()
#Click the second item in the maker page
driver.find_element_by_xpath('//div[@class="tile-container-4 tile-spacing-4 tile-container-2-mobile tile-spacing-2-mobile "]').find_elements_by_tag_name('a')[1].click()
#Select 3 items
driver.find_element_by_xpath("//select/option[text()='3']").click()
#Add them to cart
driver.find_element_by_xpath('//button[@formaction="cart.add"]').click()
#Check add-to-cart toast text
assert "3 items in your cart" in driver.find_element_by_xpath('//div[@class="flex-row flex-justify-center"]').text, "Text found: " + driver.find_element_by_xpath('//div[@class="flex-row flex-justify-center"]').text
#Close browser
driver.quit()
