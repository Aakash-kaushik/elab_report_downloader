# Author : Aakash Kaushik <https://github.com/Aakash-kaushik>
import time, os, shutil
from glob import glob
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# User ID.
email_value = r'<Your register number>'

# Password for the account.
pwd_value = r'<Password>'

# Link for the required lab 
# For example, DAA: https://care.srmist.edu.in/srmktrada
url = r'<eLab link as required>'

# Add Chrome default download path (it's better to create a new folder for this). 
# Windows: C:/Users/<username>/Downloads/<folder_name>
download_path = '<path to download the reports to>'

num_que = int(input("Enter the index number of question till which to check for reports: "))

# The options.add_argument is the default user profile that 
# can be found in a path similar to:
# Linux distros: /home/<username>/.config/google-chrome/Default
# Windows: C:/Users/<username>/AppData/Local/Google/Chrome/User Data/Default
options = Options()
options.add_argument("<path to user default profile>")
prefs = {"excludeSwitches" : "disable-popup-blocking"}
options.add_experimental_option('prefs', prefs)
options.add_argument("download.default_directory=./temp")
options.add_argument("--start-maximized")


# Get chromedriver from https://chromedriver.chromium.org/
# and add it as a PATH variable or specify the path in the
# next line in the executable_path argument. 
# If you downloaded chromedriver in Windows, the path might be:
# C:/Users/<username>/Downloads/chromedriver
driver = webdriver.Chrome(executable_path = "<chrome driver path>", desired_capabilities = DesiredCapabilities.CHROME,
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

# To click language banner as per the eLab link.
banner = driver.find_element_by_css_selector("body > app-root > div > app-student-home > div > mat-card > div > div > app-student-home-card > mat-card")
banner.click()
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

  if res_pass != "green;":
    # Try changing from c to c++, elab is on c by default.
    dropdown = driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]").click()
    cpp_select = driver.find_element_by_xpath(r'//*[@id="mat-option-1"]/span').click()

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

      # Scroll to the bottom of the page. 
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      # Downloading Report.
      report_down.click()
      time.sleep(0.5)

      report_list = glob(os.path.join(download_path,"*.png"))
      if report_list:
        new_folder_path = os.path.join(download_path, "folder_{}".format(num)) 
        os.mkdir(new_folder_path)
        for report in report_list:
          shutil.move(report, new_folder_path)
      break
  
  # Scroll to the top of the page. 
  driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
  time.sleep(5)

  # Clicking next. 
  next_but = driver.find_element_by_css_selector("body > app-root > div > app-student-solve > div.top > button:nth-child(3)")
  next_but.click()
  time.sleep(5)

driver.quit()
