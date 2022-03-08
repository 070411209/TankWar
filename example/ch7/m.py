# import webdriver
from selenium import webdriver
from PIL import Image
from io import BytesIO

# create webdriver object
driver = webdriver.Chrome()
# driver.set_window_size(800, 600)
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://segmentfault.com/q/1010000015720074")

screenshot = driver.get_screenshot_as_png()
screenshot = Image.open(BytesIO(screenshot))
driver.get_screenshot_as_file('test.png')
# get Screenshot
# print(driver.get_screenshot_as_png())
