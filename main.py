# imports our web driver dependency
from selenium import webdriver
from time import sleep
from secrets import pw


# creating a class of bot which will open new browser window. takes in username and password
class InstaBot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        # sends in username and password in their designated fields.
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        # xpath query link that contains text--'Log in' then .click clicks link
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
            .click()
        sleep(4)

    def get_unfollowers(self):
        # find a link that contains property href with value of username brackets gets replaced by username varible
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following')]".format(self.username))\
            .click()
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]');
        # passing in javascript expression to scroll through sugs varible.
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(1)
        # setting last height and height varibles
        last_ht, ht = 0, 1
        # on each scroll we want to compare the ht of the box to the ht of the box before the scroll
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
            ht  = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        
my_bot = InstaBot('clevelandboy23', pw)
# my_bot.get_unfollowers()