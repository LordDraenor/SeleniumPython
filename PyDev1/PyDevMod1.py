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
#options.add_argument("--window-size=1600,1200")
# driver=webdriver.Safari()
# driver.maximize_window()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.set_window_size(1920, 1080, 'current')

#Go to the main site and check that you're there
driver.get("https://dev.thegrommet.com")
assert "Grommet" in driver.title, "The title does not contain Grommet since it is" + driver.title
#Click the second item in the recent discoveries group
driver.find_element_by_xpath('//div[@class="tile-container-3 tile-container-2-mobile"]').find_elements_by_tag_name('a')[1].click()
#Click the second item in the maker page
driver.find_element_by_xpath('//div[@class="p-t-l p-b-s p-t-m-phone p-b-0-phone"]').find_elements_by_tag_name('a')[1].click()
#Select 3 items
driver.find_element_by_xpath("//select/option[text()='3']").click()
#Add them to cart
driver.find_element_by_xpath('//button[@formaction="cart.add"]').click()
#Check add-to-cart toast text
testEleme = driver.find_element_by_xpath('//*[@id="svelteSMNED0YE"]/div/div/div[1]/div[3]/div/div/div/div/div')                                                
assert "2 items in your cart" in testEleme.text, testEleme.text
#Close browser
driver.quit()
