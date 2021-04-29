# Author : Aakash Kaushik <https://github.com/Aakash-kaushik>
import time, os, shutil
from glob import glob
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# User id.
email_value = r'RA1911031010035'

# Password for the account.
pwd_value = r'viraj2001'

url = r'https://care.srmist.edu.in/srmktrada'

# chrome default dowload path. 
download_path = '/home/aakash/Downloads'

num_que = int(input("Enter the index number of question till which to check for reports: "))

# The options.add_argument is the defualt user profile that 
# could be found in a path similar to:
# Linux distros: /home/<username>/.config/google-chrome/Default
# Windows: need to add
options = Options()
options.add_argument("/home/aakash/.config/google-chrome/Default")
prefs = {"excludeSwitches" : "disable-popup-blocking"}
options.add_experimental_option('prefs', prefs)
options.add_argument("download.default_directory=./temp")
options.add_argument("--start-maximized")


# Get chromedriver from https://chromedriver.chromium.org/
# and add it as a PATH variable or specify the path in the
# next line in the executable_path argument. 
driver = webdriver.Chrome(executable_path = "./chromedriver", desired_capabilities = DesiredCapabilities.CHROME,
                          options = options)
driver.implicitly_wait(5)
driver.get(url)

time.sleep(4)
# Element to find email field.
email = driver.find_element_by_css_selector('#mat-input-0')
email.send_keys(email_value)

# Element to find password field.
pwd =  driver.find_element_by_css_selector('#mat-input-1') 
pwd.send_keys(pwd_value)

# To click login on the landing page.
login_but = driver.find_element_by_css_selector('body > app-root > div > app-login > div > mat-card > div.login-from > form > button')
login_but.click()
time.sleep(10)


# To click OOPS banner.
oops_banner = driver.find_element_by_css_selector("body > app-root > div > app-student-home > div > mat-card > div > div > app-student-home-card > mat-card")
oops_banner.click()
time.sleep(2)

# Clicking on the first question.
first_que = driver.find_element_by_css_selector("#svgChart > g > g:nth-child(4) > path:nth-child(100)")
first_que.click()

for num in range(num_que):
  # Clicking evaluate button.
  evaluate = driver.find_element_by_css_selector('body > app-root > div > app-student-solve > div.container > app-solve-question > div > div > div.solution > mat-card > div.main-buttons > button.mat-raised-button.mat-accent > span')
  evaluate.click()
  time.sleep(4)

  result = driver.find_element_by_css_selector('body > app-root > div > app-student-solve > div.container > app-solve-question > div > div > div.solution > mat-card > div.result.ng-star-inserted > a:nth-child(1)')
  res_pass = result.get_attribute("style").split(" ")[-1]
  if res_pass == "green;":
    # Download report button.
    report_down = driver.find_element_by_css_selector('body > app-root > div > app-student-solve > div.container > app-solve-question > div > div > div.solution > mat-card > div.result.ng-star-inserted > a.result.mat-elevation-z2.ng-star-inserted')
    while True:

      # Scroll to the botton of the page. 
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      # Downloading Report
      report_down.click()
      time.sleep(0.5)
      report_list = glob(os.path.join(download_path,"*.png"))
      if report_list:
        new_folder_path = os.path.join(download_path, "folder_{}".format(num)) 
        os.mkdir(new_folder_path)
        for report in report_list:
          shutil.move(report, new_folder_path)
        break

  # Clicking next. 
  time.sleep(8)
  next_but = driver.find_element_by_css_selector("body > app-root > div > app-student-solve > div.top > button:nth-child(3)")
  next_but.click()
  time.sleep(5)

driver.quit()
