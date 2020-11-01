# Author : Aakash Kaushik <https://github.com/Aakash-kaushik>
import time
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# User id.
email_value = r'<user id>'

# Password for the account.
pwd_value = r'<password>'

url = r'https://care.srmist.edu.in/srmktroops'

# chrome default dowload path. 
download_path = '<chrome default download path>'

num_que = int(input("enter the number of questions to download: ")) - 1 

# The options.add_argument is the defualt user profile that 
# could be found in a path similar to:
# Linux distros: /home/<username>/.config/google-chrome/Default
# Windows: need to add
options = Options()
options.add_argument("<default profile>")
prefs = {"excludeSwitches" : "disable-popup-blocking"}
options.add_experimental_option('prefs', prefs)
options.add_argument("download.default_directory=./temp")
options.add_argument("--start-maximized")


# Get chromedriver from https://chromedriver.chromium.org/
# and add it as a PATH variable or specify the path in the
# next line in the executable_path argument. 
driver = webdriver.Chrome(executable_path = "<chromedriver path>", desired_capabilities = DesiredCapabilities.CHROME,
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

# Clicking evaluate button for first question.
evaluate = driver.find_element_by_css_selector('body > app-root > div > app-student-solve > div.container > app-solve-question > div > div > div.solution > mat-card > div.main-buttons > button.mat-raised-button.mat-accent > span')
evaluate.click()
time.sleep(4)

result = driver.find_element_by_css_selector('body > app-root > div > app-student-solve > div.container > app-solve-question > div > div > div.solution > mat-card > div.result.ng-star-inserted > a:nth-child(1)')
res_pass = result.get_attribute("style").split(" ")[-1]
if res_pass == "green;":
  # Download report button for first question.
  report_down = driver.find_element_by_css_selector('body > app-root > div > app-student-solve > div.container > app-solve-question > div > div > div.solution > mat-card > div.result.ng-star-inserted > a.result.mat-elevation-z2.ng-star-inserted')
  while True:
    # Downloading Report for first question.
    report_down.click()
    time.sleep(0.5)
    if path.isfile(path.join(download_path, "report.png")):
      break

# Clicking next on the first question page.
time.sleep(8)
next_but = driver.find_element_by_css_selector("body > app-root > div > app-student-solve > div.top > button:nth-child(3)")
next_but.click()
time.sleep(5)

# variable to keep track of downloads, don't change.
reports_downloaded = 1

for _ in range(num_que):
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
      # Downloading Report
      report_down.click()
      time.sleep(0.5)
      if path.isfile(path.join(download_path, "report ({}).png".format(reports_downloaded))):
        reports_downloaded += 1
        break

  # Clicking next. 
  time.sleep(8)
  next_but = driver.find_element_by_css_selector("body > app-root > div > app-student-solve > div.top > button:nth-child(3)")
  next_but.click()
  time.sleep(5)
