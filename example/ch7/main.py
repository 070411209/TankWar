# -*- coding: utf-8 -*-
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
get_html = "test.html" 
f = open(get_html,'wb')

browser = webdriver.Chrome(options=chrome_options)
# 设置隐式等待，超时10秒
wait = WebDriverWait(browser, 10)
browser.get("https://www.baidu.com/")
# 点击搜索按钮
input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
input.send_keys("python")
time.sleep(2)
f.write(browser.page_source.encode("gbk", "ignore"))
# # 关闭浏览器
browser.close()
print("执行完成")
f.close() 