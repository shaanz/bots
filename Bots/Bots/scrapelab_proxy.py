from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

#proxy1 = Proxy()
proxy1 = ["54.254.169.21:8888", "proxy2:0"]
chrome_options = webdriver.ChromeOptions()


try :
	i = 0
	count = 1
	while True :
		i = i + 1
		print ('Accessing Article ' + str(i))
		chrome_options.add_argument('--proxy-server=%s' %proxy1[0])
		browser = webdriver.Chrome(options=chrome_options)
		browser.get("https://www.f5.com/labs/articles/threat-intelligence/jwt--a-how-not-to-guide")
		#browser.get("https://httpbin.org/ip")
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
		if i >= count:
			break	
except Exception as e:
	print('Iteration Failed')	
	print(e)