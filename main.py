from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import Login

browser = webdriver.Chrome('./chromedriver')
# browser.get('http://linkedin.com')
browser.get('https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin')
sleep(1)    # wait for html to load
try:
    browser.find_element_by_link_text('Sign in').click()
    sleep(1)

    browser.find_element_by_id('username').send_keys(Login.username)
    sleep(1)

    browser.find_element_by_id('password').send_keys(Login.pwd)
    sleep(1)

    browser.find_element_by_xpath("//button[@type = 'submit']").click()
    sleep(3)

finally:

    # get into the file
    browser.find_element_by_xpath("//input[@type='text']").send_keys('nyu')
    sleep(1)

    browser.find_element_by_xpath("//input[@type='text']").send_keys(Keys.RETURN)
    sleep(4)

    browser.find_element_by_xpath("//button[text() = 'People']").click()
    sleep(3)

# try to connect to one person
# browser.find_element_by_xpath("//span[text() = 'Connect']/..").click()
# sleep(1)
#
# browser.find_element_by_xpath("//span[text() = 'Add a note']/..").click()
# sleep(1)
#
# browser.find_element_by_xpath("//textarea[@name='message']").send_keys('Hello')
# sleep(1)
#
# browser.find_element_by_xpath("//button[@aria-label='Dismiss']").click()
# sleep(1)

# Send the message
# browser.find_element_by_xpath("//span[text() = 'Send']/..").click()
# sleep(1)


# test click next
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# sleep(2)
# browser.find_element_by_xpath("//button[@aria-label='Next']").click()



# try to connect to multiple person
people = browser.find_elements_by_xpath("//span[text() = 'Connect']/..")
sleep(2)

for person in people:
    person.click()
    sleep(1)
    browser.find_element_by_xpath("//span[text() = 'Add a note']/..").click()
    sleep(1)
    browser.find_element_by_xpath("//textarea[@name='message']").send_keys('Hello')
    sleep(1)
    browser.find_element_by_xpath("//button[@aria-label='Dismiss']").click()
    sleep(1)
#
# sleep(2)
# browser.find_element_by_xpath("//button[@aria-label='Next']").click()
# sleep(1)




