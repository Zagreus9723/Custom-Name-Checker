import time
from selenium import webdriver
import random
import os
site = input("What site do you want to check names for and how is it formatted? IE: https://solo.to\n[?]:")
response = input("What is the title or the first few words of the page when the name is not registered? IE: Page Not Found, or if it is blank just hit enter.\n[?]:")
wait = input("How many secons do you want to wait between each check:\n[?]:")
file = input("What is the name of your file? Include the .txt\n[?]:")
if os.path.exists(file):
    mode = int(input("How do you want to load your links?\n[1]: Links\n[2]: Just the names\n[?]: "))
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
    if mode == 1:
        with open(site, 'r') as handle:
            codes = handle.readlines()
            for x in codes:
                driver.get(f"{x}")
                e = driver.title
                if f"{response} in f"{e}":
                    r = open('valid.txt', 'a')
                    r.write("------------------------\n")
                    r.write(f"{x}\n")
                    r.close()
                    time.sleep(wait)
                else:
                    ()
    elif mode == 2:
        with open(file, 'r') as handle:
            codes = handle.readlines()
            for x in codes:
                driver.get(f"{site}{x}")
                e = driver.title
                if f"{response} in f"{e}":
                    r = open('valid.txt', 'a')
                    r.write("------------------------\n")
                    r.write(f"{site}{x}\n")
                    r.close()
                    time.sleep(wait)
                else:
                    ()
    else:
        print("Wrong number!")
else:
    print(f"Please create and add words or links to {file}.")
