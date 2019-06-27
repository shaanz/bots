# bots
Work in progress bots for simple demo of 
1) Account Aggregation - Needs Selenium installed on machine 
2) Brute Force - Needs Hydra Installed 
3) WebInjects  - Requires NodeJS and Tamper Monkey plugin on chrome 

PREREQ
-----------

Steps to Install Selenium on Mac
--------------------------------------

1. brew install python
2. Python -V
3.  Adding WebDriver
     pip3 install selenium
         If you get an error, you may need to perform the pip installfor python3. Try this: curl -O https://bootstrap.pypa.io/get-pip.py

4. sudo python3 get-pip.py

5. Adding ChromeDrive 
      Download and Put Chromedriver in Path : http://chromedriver.chromium.org/downloads

6. All set to run Account Aggregation code with 
    python3 createaccunt.py 

Steps to Run Web Inject 
--------------------------------------
1. Install Nodejs 
2. Run nodejs democc.js
2. Install Tamper Monkey Plugin and Configure the script provided via dashboard 

