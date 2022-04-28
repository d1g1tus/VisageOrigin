import os
import random
import string
import ssl
import sys
import urllib
import win32clipboard
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import request


class Mf:

    @staticmethod
    def start():
        global browser
        # proxy = "85.25.150.32:5566"
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_argument(f"window-size={random.randint(800, 1300)},{random.randint(200, 700)}")
        option.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

        #option.add_argument('--proxy-server=%s' % proxy)
        browser = webdriver.Chrome(options=option)



    @staticmethod
    def password():
        random.seed(random.randint(0, 10000))
        caps = ["A", "B", "C", "D"]
        letters = string.ascii_lowercase
        rand_letters = random.choices(letters, k=9)
        return "".join(caps[random.randint(0, 3)] + "".join(rand_letters) + str(random.randint(1, 100)))

    @staticmethod
    def username():
        random.seed(random.randint(0, 10000))
        caps = ["A", "B", "C", "D"]
        letters = string.ascii_lowercase
        rand_letters = random.choices(letters, k=9)
        return "".join(caps[random.randint(0, 3)] + "".join(rand_letters) + str(random.randint(1, 100)))

    @staticmethod
    def checkmail(mail):
        mails = ["barooko.com", "washort.com", "batouty.com"]
        banmail = ["lookacross.net", "ofisher.net"]
        parsed = mail[0:]
        for i in range(len(parsed)):
            if parsed[i] == "@":
                pos = parsed.index(parsed[i])
                domain = "".join(parsed[pos+1:])
                if domain in mails:
                    print(f"//// Using {domain} domain")
                if domain in banmail:
                    print(f"//// Using a restricted domain ({domain}). Starting process again")
                    for handle in browser.window_handles:
                        browser.switch_to.window(handle)
                        browser.close()
                    Mf.start()
                    return main()


def main():

    browser.execute_script("window.open('https://www.receivemail.org/','firstab');")
    browser.execute_script("window.open('https://store.steampowered.com/join','secondtab');")

    browser.switch_to.window("firstab")

    while True:
        try:
            browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/button").click()
            break
        except:
            pass

    time.sleep(2)
    if way1:
        browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[1]/div[2]/button/span[1]").click()
    if way2:
        browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[1]/input").send_keys(usrnam)
        browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[1]/select").send_keys("w")
        browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[1]/button").click()

    time.sleep(4)
    clip = browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[3]/strong/span").text
    Mf.checkmail(clip)

    browser.switch_to.window("secondtab")
    time.sleep(1)
    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[2]/div/input").send_keys(clip)
    time.sleep(random.randint(1,5))
    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[3]/div/input").send_keys(clip)
    time.sleep(random.randint(1,5))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[6]/div[1]/label/input").click()
    time.sleep(random.randint(1,5))
    browser.execute_script("window.scrollTo(0, 25);")
    time.sleep(random.randint(1,5))
    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[5]/div/div[1]/div/div/div/iframe").click()
    os.system("pause")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[6]/div[2]/button").click()

    browser.switch_to.window("firstab")

    while True:
        try:
            browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[4]/div").click()
            time.sleep(2)
            browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[4]/div/div/div/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a/span").click()
            time.sleep(2)
            browser.close()
            break
        except:
            pass

    browser.switch_to.window("secondtab")
    time.sleep(3)
    browser.find_element(by=By.XPATH, value="/html/body/div/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[2]/div[1]/input").send_keys(usrnam)
    time.sleep(random.randint(1,5))
    browser.find_element(by=By.XPATH, value="/html/body/div/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[3]/div[1]/input").send_keys(paswd)
    time.sleep(random.randint(1,5))
    browser.find_element(by=By.XPATH, value="/html/body/div/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[4]/div[1]/input").send_keys(paswd)
    time.sleep(random.randint(1,5))
    browser.find_element(by=By.XPATH, value="/html/body/div/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[5]/div/button/span").click()
    print(f"///// Username -> {usrnam}")
    print(f"///// Password -> {paswd}")

if __name__ == '__main__':

    Mf.start()
    win32clipboard.OpenClipboard()
    usrnam = Mf.username()
    paswd = Mf.password()
    way1 = bool(False)
    way2 = bool(True)
    main()


