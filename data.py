import time
import pandas as pd
from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument ( "--headless") # 开启无界面模式
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
drive = webdriver.Chrome(service=service, options=option)
key_word = '大数据算法'
url = 'https://we.51job.com/pc/search?keyword={}&searchType=2&sortType=0&metro='.format(key_word)
drive.get(url)
time.sleep(3)
names, salarys, tags, company, zhuying, xingzhi, xuqiu, where = [], [], [], [], [], [], [], []
def get_data():
    time.sleep(2)
    jnames = drive.find_elements(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.joblist > div > div.joblist-item-job.sensors_exposure > div.joblist-item-top > span.jname.text-cut')
    jsalarys = drive.find_elements(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.joblist > div > div.joblist-item-job.sensors_exposure > div.joblist-item-top > span.sal.shrink-0')
    jtags = drive.find_elements(By.CLASS_NAME, 'tags')
    jcompany = drive.find_elements(By.CSS_SELECTOR, "#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.joblist > div > div.joblist-item-job.sensors_exposure > div.joblist-item-bot > div.bl > a")
    jzhuying = drive.find_elements(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.joblist > div > div.joblist-item-job.sensors_exposure > div.joblist-item-bot > div.bl > span.dc.text-cut')
    jxingzhi = drive.find_elements(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.joblist > div > div.joblist-item-job.sensors_exposure > div.joblist-item-bot > div.bl > span:nth-child(4)')
    jxuqiu = drive.find_elements(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.joblist > div > div.joblist-item-job.sensors_exposure > div.joblist-item-bot > div.bl > span:nth-child(5)')
    jwhere = drive.find_elements(By.CSS_SELECTOR, '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div:nth-child(2) > div.joblist > div > div.joblist-item-job.sensors_exposure > div.joblist-item-bot > div.br > div > div')
    print(jnames[0].text)
    for _ in range(len(jnames)):
        try:
            names.append(jnames[_].text)
        except:
            names.append('无')
        try:
            salarys.append(jsalarys[_].text)
        except:
            salarys.append('无')
        try:
            tags.append(jtags[_].text)
        except:
            tags.append('无')
        try:
            company.append(jcompany[_].text)
        except:
            company.append('无')
        try:
            zhuying.append(jzhuying[_].text)
        except:
            zhuying.append('无')
        try:
            xingzhi.append(jxingzhi[_].text)
        except:
            xingzhi.append('无')
        try:
            xuqiu.append(jxuqiu[_].text)
        except:
            xuqiu.append('无')
        try:
            where.append(jwhere[_].text)
        except:
            where.append('无')


get_data()
for _ in range(49):
    try:
        drive.find_element(By.CSS_SELECTOR,
                       '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div.bottom-page > div > div > div > button.btn-next').click()
    except:
        time.sleep(5)
        drive.find_element(By.CSS_SELECTOR,
                           '#app > div > div.post > div > div > div.j_result > div > div:nth-child(2) > div > div.bottom-page > div > div > div > button.btn-next').click()
    get_data()

data = [names, salarys, tags, company, zhuying, xingzhi, xuqiu, where]
df = pd.DataFrame(data).T
header = ['职位', '薪资', '标签', '公司', '主营', '性质', '需求', '地点']
df.to_excel('./大数据/{}.xlsx'.format(key_word), index=False, header=header)
