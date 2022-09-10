import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import os

url = "https://www.facebook.com/"
email = "reson456@gmail.com"
password = "asd102045"

# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)
# 最大化視窗
driver.maximize_window()
# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element("id","email").send_keys(email)
driver.find_element("id","pass").send_keys(password)
driver.find_element("name","login").click()

time.sleep(5)

# 進入木棉花專頁
driver.get("https://www.facebook.com/emuse.com.tw")

time.sleep(5)

#滑動
for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(2)


#獲得網頁碼
soup = BeautifulSoup(driver.page_source,"html.parser")
#定位標題
titles = soup.find_all("div", class_ = "m8h3af8h l7ghb35v kjdc1dyq kmwttqpk gh25dzvf n3t5jt4f")
for title in titles:
    #每一行
    posts = title.find_all("div",dir="auto")
    if(len(posts)):
        for post in posts:
            print(post.text)

    print("-"*30)
# 建立資料夾
if not os.path.exists("images"):
    os.mkdir("images")
#抓圖片
images = soup.find_all("img", class_="z6erz7xo on4d8346 pytsy3co s8sjc6am myo4itp8 ekq1a7f9 mfclru0v")
if len(images) != 0:
    for index,image in enumerate(images):
        img = requests.get(image["src"])
        with open(f"images/img{index+1}.jpg", "wb") as file:
            file.write(img.content)
        print(f"第 {index+1} 張圖片下載完成!")