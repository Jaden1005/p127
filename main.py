from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
#browser = webdriver.Chrome("/chromedriver")
driver.get(start_url)
time.sleep(10)
def scrape():
    headers = ["name","distance","mass","radius"]
    planetdata = []
    for i in range(0,208):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs = ("class","exoplanet")):
            li_tags = ul_tag.find_all("li")
            templist = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(li_tag.contents[0])
                    except:
                        templist.append("")
            planetdata.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper_2.csv","w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerow(planetdata)
    scrape()