from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

try :
	i = 0
	count = 100
	while True :
		i = i + 1
		print ('Accessing Article ' + str(i))
		browser = webdriver.Chrome()
		browser.get("https://www.f5.com/labs/articles/threat-intelligence/jwt--a-how-not-to-guide")
		time.sleep(20)
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
		time.sleep(20)
		browser.execute_script("window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight);")            

	    #username = browser.find_element_by_name('username')
	    #username.send_keys(usernamekey+str(i)+'@demohack.com')
	    #register = browser.find_element_by_name('register')
	    #register.click();
		browser.implicitly_wait(1000)
		time.sleep(30)
		browser.quit()
		print('Done Round' + str(i))
		if i > count:
			break	
except Exception as e:
	print('Iteration Failed')	
	print(e)