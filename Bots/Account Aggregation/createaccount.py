from   selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from   selenium.common.exceptions import TimeoutException
  
#browser = webdriver.Chrome()
#browser = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
try :
    i = 0
    count =10
    usernamekey = 'Ranger8'
    while True :
	    i += 1
	    print ('Attempting Account Creation: ' + str(i))
	    browser = webdriver.Chrome()
	    
	    browser.get("http://18.138.20.63/#/signup/0")
	    

	    username = browser.find_element_by_name('username')
	    username.send_keys(usernamekey+str(i)+'@demohack.com')

	    firstname = browser.find_element_by_name('firstname')
	    firstname.send_keys(usernamekey + str(i))

	    lastname = browser.find_element_by_name('lastname')
	    lastname.send_keys("Cracker" + str(i))


	    email = browser.find_element_by_name('email')
	    email.send_keys('demouser'+str(i)+'@demohack.com')


	    phonenumber = browser.find_element_by_name('phonenumber')
	    phonenumber.send_keys("6666666666");

	    password = browser.find_element_by_name('password')
	    password.send_keys("password");

	    cnfpassword = browser.find_element_by_name('cnfpassword')
	    cnfpassword.send_keys("password");

	    address = browser.find_element_by_name('address')
	    address.send_keys("Singapore");

	    zipcode = browser.find_element_by_name('zipcode')
	    zipcode.send_keys("142637");

	    register = browser.find_element_by_name('register')
	    register.click();

	  
	    browser.implicitly_wait(10)
	    browser.quit()
	    if i > count:
		    break	
except Exception as e:
    print('Iteration Failed')	
    print(e.message)

