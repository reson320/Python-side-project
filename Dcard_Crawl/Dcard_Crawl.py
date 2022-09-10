import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#Proxy ip變動需求
#網頁設定
url = "https://www.dcard.tw/f/nctu"
email = "reson320@gmail.com"
password = "zxc4621719"
#driver安裝
driver = webdriver.Chrome(ChromeDriverManager().install())
#進入網頁
driver.get(url)
time.sleep(30)
#登入
driver.find_element("partial link text","註冊 / 登入").click()
time.sleep(3)
driver.find_element("id","email").send_keys(email)
driver.find_element("id","password").send_keys(password)
driver.find_element("css selector","[type=\"submit\"]").click()
time.sleep(3)
#獲得soup
soup = BeautifulSoup(driver.page_source,"html.parser")
#爬文章
posts = soup.find_all("article",class_ = "sc-4e60752d-0 gWKNlb")
for post in posts:
    post_url = "https://www.dcard.tw"+post.a["href"]
    r = requests.get(post_url)
    rs = BeautifulSoup(r.text,"html.parser")
    #文章資訊
    author = rs.find("div", class_ = "sc-a2793d22-4 fEVQiQ").text
    title = rs.find("h1", class_ = "sc-ae7e8d73-0 dZLSBh").text
    board = rs.find_all("div",class_ = "sc-488ede4a-4 fizJhx")[0].text
    post_time = rs.find_all("div", class_ = "sc-488ede4a-4 fizJhx")[1].text
    print("-"*30)
    print("標題:"+title)
    print("文章作者:"+author)
    print("看板:"+board+"   發文時間:"+post_time)
    #內文
    content = rs.find("div", class_ = "sc-ba53eaa8-0 iSPQdL").text
    print("\n內文:\n"+content)
    #時間等待
    time.sleep(2)

