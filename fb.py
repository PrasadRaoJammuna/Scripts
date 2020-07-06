# Auto Posting in Facebook


from selenium import webdriver
from secrete import email,pwd
import time


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.facebook.com/')

user =  driver.find_element_by_id('email')
user.send_keys(email)


password = driver.find_element_by_id('pass')
password.send_keys(pwd)


button = driver.find_element_by_id('u_0_b')
button.submit()

time.sleep(10)


body =  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]')
body.click()

time.sleep(5)

message = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
message.send_keys('https://youtu.be/RI_MFRNnDiI')

time.sleep(10)

post = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div')
post.click()

#driver.close()














































































'''
from selenium import webdriver
import time
from secrate import email,pwd


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.facebook.com/')

user = driver.find_element_by_id('email')
user.send_keys(email)

password = driver.find_element_by_id('pass')
password.send_keys(pwd)


button = driver.find_element_by_id('u_0_b')
button.submit()

time.sleep(10)

feed = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]')
feed.click()

time.sleep(10)

post = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
post.send_keys('Test: Automation Testing..!')


send = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div')
send.submit()

#driver.close()

'''



