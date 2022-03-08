# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# #声明浏览器对象
browser1 = webdriver.Chrome()
get_html = "baidu.html"
f = open(get_html, 'wb')
# #访问页面
browser1.get("https://time.geekbang.org/column/article/76001")
time.sleep(2)
print(browser1.page_source)
f.write(browser1.page_source.encode("gbk", "ignore"))  # 忽略非法字符
# 关闭当前窗口
browser1.close()
f.close()
