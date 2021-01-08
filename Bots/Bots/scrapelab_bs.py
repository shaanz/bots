from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

try :
	i = 0
	count = 50
	while True :
		i = i + 1
		print ('Accessing Article ' + str(i))
		browser = webdriver.Chrome()
		browser.get("https://www.f5.com/labs/search?q=kristen+ludwick")
	
		browser.implicitly_wait(1000)
		time.sleep(30)
		browser.quit()
		print('Done Round' + str(i))
		if i > count:
			break	
except Exception as e:
	print('Iteration Failed')	
	print(e)