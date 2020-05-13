from selenium import webdriver
from selenium.webdriver import Firefox
import time
from creds import mail, password #Importing the creds to use them later.

def loginYouTube():
	driver=webdriver.Firefox()
	driver.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dfr%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=fr&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')				
	login=driver.find_element_by_xpath('//*[@id="identifierId"]')
	login.send_keys(mail)
	nextbutton=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
	time.sleep(3)
	nextbutton.click()
	time.sleep(1)
	window_after = driver.window_handles[0]
	driver.switch_to.window(window_after)
	passwordbox=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
	passwordbox.send_keys(password)
	submitbutton=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span')
	time.sleep(3)
	submitbutton.click()
	time.sleep(3)


loginYouTube()
