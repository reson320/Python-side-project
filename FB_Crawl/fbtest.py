from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

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
driver.find_element("id","email").send_keys(email)
driver.find_element("id","pass").send_keys(password)
driver.find_element("name","login").click()

time.sleep(5)
#個人資料
driver.get("https://www.facebook.com/emuse.com.tw")
time.sleep(5)


#點讚
driver.find_element("css selector","[aria-label=\"讚\"]").click()


time.sleep(10)