import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wait = 5

# Variable declaration
url = "https://automationplayground.com/crm/login.html"
email_address = "williamshakespare@gmail.com"
password = "test123"
new_customer_email = "helen247@gmail.com"
first_name = "Helen"
last_name = "Jones"
city = "Lagos"

# Browser initialisation
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

#Login details
EmailAddress = driver.find_element(By.ID, "email-id")
EmailAddress.send_keys(email_address)
Password = driver.find_element(By.ID, "password")
Password.send_keys(password)
Submit = driver.find_element(By.ID, "submit-id")
Submit.click()
time.sleep(wait)

#Create new customer
NewCustomer = driver.find_element(By.ID, "new-customer")
NewCustomer.click()

# Add Customer / Fill Customer form
NewCustomer_email = driver.find_element(By.ID, "EmailAddress")
NewCustomer_email.send_keys(new_customer_email)

FirstName = driver.find_element(By.ID, "FirstName")
FirstName.send_keys(first_name)

LastName = driver.find_element(By.ID, "LastName")
LastName.send_keys(last_name)

City = driver.find_element(By.ID, "City")
City.send_keys(city)

SubmitCustomer = driver.find_element(By.CSS_SELECTOR, "#loginform > div > div > div > div > form > button")
SubmitCustomer.click()
time.sleep(wait)

# Log Out
SignOut = driver.find_element(By.CSS_SELECTOR, "body > nav > ul > li > a")
SignOut.click()
time.sleep(wait)
