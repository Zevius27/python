from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def fileHelperHtml(fileName):

    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://gofile.io/d/{fileName}")
    sleep(3)
    elem = driver.find_element(
        By.ID, "filemanager_itemslist").get_attribute("innerHTML")
    # print(elem)
    driver.close()
    htmlString = str(elem)
    print(htmlString)
    return htmlString


# fileHelperHtml()
