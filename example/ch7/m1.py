from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

drive = webdriver.Chrome()
url = 'http://www.baidu.com/'
drive.get(url)
#获取当前窗口所有句柄
handles = drive.window_handles
#通过句柄 切换到第2个标签页
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-infobars')

# drive.save_screenshot("a.png")
# sc_str = drive.get_screenshot_as_png()
drive.get("https://www.baidu.com/")
drive.get_screenshot_as_png("c.png")
# print(drive.get_screenshot_as_png())

sc_path = "b.png"
with open(sc_path,"w") as f:    
    f.write(sc_str)
drive.close()
