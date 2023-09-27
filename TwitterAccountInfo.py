import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import re


class TwitterAccountInfo:
    def __init__(self):
        self.date = None
        self.follow = None
        self.follower = None
        self.icon = None
        self.description = None
        self.userName = None
        self.userid = None

    def getScreenName(self, user_id):
        browser = webdriver.Chrome()
        find = browser.find_element
        browser.get("https://tweeterid.com")
        time.sleep(3)
        find(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form/input").send_keys(user_id)
        time.sleep(1)
        find(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div[1]/div").click()
        time.sleep(5)
        id_to_name = find(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/p[2]").text
        usr = id_to_name.find("@")
        browser.close()
        return id_to_name[usr + 1:]

    def getAccountInfo(self, screen_name):
        try:
            browser = webdriver.Chrome()
            browser.get("https://twiteridfinder.com/")
            find = browser.find_element
            find(by=By.XPATH, value='//*[@id="tweetbox2"]').send_keys(screen_name)
            time.sleep(2)
            browser.execute_script("submitData()")
            time.sleep(10)
        except:
            return "error"
        self.userid = find(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/div[2]').text
        self.userName = find(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/div[3]/a').text
        self.description = find(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/div[4]').text
        follow_count = find(by=By.XPATH, value='/html/body/div[2]/div/div[3]/div/div[6]').text
        self.icon = find(by=By.XPATH, value="/html/body/div[2]/div/div[3]/div/img").get_attribute("src")
        self.date = find(by=By.XPATH, value="/html/body/div[2]/div/div[3]/div/div[7]").text
        ff = follow_count.split()
        self.follower = re.sub(r"\D", "", ff[3])
        self.follow = re.sub(r"\D", "", ff[0])

        browser.close()
        return {"Screen Name": self.userName, "User Id": self.userid, "Description": self.description,
                "follow": self.follow, "follower": self.follower, "accountDate": self.date, "icon": self.icon}


if __name__ == "__main__":
    print("a")
