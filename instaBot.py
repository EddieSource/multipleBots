from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import Login

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.instagram.com/')

sleep(1)    # wait for html to load

browser.find_element_by_xpath("//input[@aria-label = 'Phone number, username, or email']").send_keys(Login.ins_username)
sleep(1)
browser.find_element_by_xpath("//input[@aria-label = 'Password']").send_keys(Login.ins_pwd)
sleep(1)

browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(4)

try:
    browser.find_element_by_xpath("//button[text()='Not Now']").click()
    sleep(3)
except:
    pass

try:
    browser.find_element_by_xpath("//button[text()='Not Now']").click()
    sleep(2)
except:
    pass


search_box = browser.find_element_by_xpath("//input[@placeholder ='Search']")
sleep(1)
search_box.send_keys("#cabinets")
sleep(1)
search_box.send_keys(Keys.RETURN)
sleep(1)
search_box.send_keys(Keys.RETURN)
sleep(5)

posts = browser.find_element_by_xpath("//article[@class]")
sleep(1)

# number of comments made so far
i = 0

while(1):
    cur_posts = posts.find_elements_by_xpath(".//a[@href]")
    sleep(2)
    for post in cur_posts:
        try:
            post.click()
            sleep(1)
            browser.find_element_by_xpath("//textarea[@aria-label = 'Add a comment…']").click()
            sleep(2)
            browser.find_element_by_xpath("//textarea[@aria-label = 'Add a comment…']").send_keys('Hi')
            sleep(2)
            # browser.find_element_by_xpath("//button[text()='post']").click()
            # sleep(1)
            browser.find_element_by_xpath("//*[local-name()='svg' and @aria-label = 'Close']/../..").click()
            sleep(1)
            i += 1
        except:
            browser.find_element_by_xpath("//*[local-name()='svg' and @aria-label = 'Close']/../..").click()
            sleep(1)

    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(2)




