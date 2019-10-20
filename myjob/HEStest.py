from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
driver = webdriver.Chrome(options=options)
driver.get("https://dhse.gdg.com.cn/Login/login")
driver.maximize_window
# driver.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys("123456789")

# driver.find_element_by_css_selector(".SignFlow-passwordInput.Input-wrapper input").send_keys("256398")



# button = driver.find_element_by_class_name('.SignFlow-tab--active')
# button.click()
element = driver.find_element_by_name('loginname').send_keys("12030059") #189对应123密码

pwd = driver.find_element_by_id('loginpwd').send_keys('zdlx3607')

# time.sleep(3)
sub1 = driver.find_element_by_css_selector('#btnlogin').click() #登录
time.sleep(3)
yinhuan = driver.find_element_by_css_selector('#side-menu > li:nth-child(7) > a > span.nav-label').click()  #隐患管理
time.sleep(3)
dangrou = driver.find_element_by_css_selector('#side-menu > li.active > ul > li:nth-child(2) > a').click()   #隐患处理

time.sleep(2)
body = driver.find_element_by_css_selector('#dealWithGrid > tbody')
for i in range(14):
    c = 'row' + str(i)
    col = body.find_element_by_id(c)
    print(col.text)
    time.sleep(4)
    deal = col.find_element_by_css_selector('#td:nth-child(10) > div > a:nth-child(2)').click()  #2019年10月12日，本处失败。
    driver.back
    time.sleep(3)
    yinhuan = driver.find_element_by_css_selector('#side-menu > li:nth-child(7) > a > span.nav-label').click()  #隐患管理
    time.sleep(3)
    dangrou = driver.find_element_by_css_selector('#side-menu > li.active > ul > li:nth-child(2) > a').click()   #隐患处理

# col0 = body.find_element_by_id('row0')
# deal = col0.find_element_by_css_selector('#row0 > td:nth-child(10) > div > a:nth-child(2)').click()  #进入到隐患处理详细页面#row0 > td:nth-child(10) > div > a:nth-child(2)

# #dealWithGrid > tbody  #row0   #row0  //*[@id="row0"]
# pwd = driver.find_element_by_id('spm6').click() #选择报表一栏=spm6  #day > span > input.textbox-text.textbox-text-readonly.validatebox-text////*[@id="day"]/span/input[1]
# display = driver.find_element_by_css_selector('#btn_hourDataSearch > span > span.l-btn-text').click()  #显示报表在页面
# #but1 = driver.find_elements_by_css_selector('#day > span').click()  #选择到时间按钮，并弹出时间控件
# unit2 = driver.find_element_by_css_selector('#_easyui_tree_2 > span.tree-title').click() #点击第二台机组
# display = driver.find_element_by_css_selector('#btn_hourDataSearch > span > span.l-btn-text').click()  #显示报表在页面

# num = driver.find_elements_by_css_selector('#idReportView > div > table > tbody > tr:nth-child(8) > td:nth-child(3)')


# #print(html)/html/body/div[4]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/table/tbody/tr/td[5]/span/input[1]

# from os import path
# from flask import Flask
# app = Flask(__name__)
# @app.route('/') #构建一个简单的网页
# # def hello_world():
# #     return 'Hello World!'
# def index():
#     try:
#         path_this = path.dirname(path.abspath(__file__))
#         path_file = path.join(path_this,"index.html")
#         fobj = open(path_file,'rb')
#         data = fobj.read()
#         fobj.close()
#         return data
#     except Exception as err:
#         return str(err)
# if __name__ == '__main__':
#     app.run(debug=True, port='5000', host='127.0.0.1')