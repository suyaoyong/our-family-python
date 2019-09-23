from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait  #这个引入用于确定网页打开后定位到某个元素
import time
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
driver = webdriver.Chrome(options=options)
driver.get("http://www-app3.gdep.gov.cn:8080")
# driver.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys("123456789")

# driver.find_element_by_css_selector(".SignFlow-passwordInput.Input-wrapper input").send_keys("256398")



# button = driver.find_element_by_class_name('.SignFlow-tab--active')
# button.click()
element = driver.find_element_by_name('UserName').send_keys("66998758-0")
pwd = driver.find_element_by_id('ViewPassword').send_keys('zdlxajh')

time.sleep(2)
sub1 = driver.find_element_by_id('btnSubmit').click() #登录网站
#sub = driver.find_elements_by_class_name('submit_btn').click()
 #等待登录时间，这个方法虽然不太好，以后再改
driver.maximize_window()  #窗口最大化
# try:
#     element = WebDriverWait(driver, 10).until(lambda x : x.find_element_by_id("spm6")) #通过这个方式确定找到元素后才进行下一步。减少时间浪费。选择报表一栏
#     element.click()
# finally:
#     time.sleep(10)
#     driver.quit()
time.sleep(2) 
pwd = driver.find_element_by_id('spm6').click() #选择报表一栏=spm6  #day > span > input.textbox-text.textbox-text-readonly.validatebox-text////*[@id="day"]/span/input[1]
# try:
#     display = WebDriverWait(driver, 10).until(lambda x : x.find_element_css_selector('#btn_hourDataSearch > span > span.l-btn-text')) #显示报表在页面
#     display.click()
# finally:
#     time.sleep(10)
#     driver.quit()
display = driver.find_element_by_css_selector('#btn_hourDataSearch > span > span.l-btn-text').click()  #显示报表在页面
#but1 = driver.find_elements_by_css_selector('#day > span').click()  #选择到时间按钮，并弹出时间控件
# try:
#     display = WebDriverWait(driver, 10).until(lambda x : x.find_element_css_selector('#idReportView > div > table > tbody')) #显示报表在页面
#     display.click()
# finally:
#     time.sleep(10)
#     driver.quit()
table1 = driver.find_element_by_css_selector('#idReportView > div > table > tbody')#获取整个表格元素#idReportView > div > table > tbody > tr:nth-child(35)

time.sleep(2) 
rows = table1.find_elements_by_css_selector('tr')#这样就获取了整个表格的数据，通过col1[i].text可以获取全部数据
row_str = []  #定义一个空列表准备作为数据容器
for row in rows:
    row_str.append(row.text)
    
for i in range(7,35):
    str_num = row_str[i].split()
    print(str_num)




# unit2 = driver.find_element_by_css_selector('#_easyui_tree_2 > span.tree-title').click() #点击第二台机组
# display = driver.find_element_by_css_selector('#btn_hourDataSearch > span > span.l-btn-text').click()  #显示报表在页面

# num = driver.find_elements_by_css_selector('#idReportView > div > table > tbody > tr:nth-child(8) > td:nth-child(3)')


#print(html)/html/body/div[4]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/table/tbody/tr/td[5]/span/input[1]

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