from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tages: ')
url = f'https://www.instagram.com/explore/tags/{tag}'

service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service) #service 라는 속성 안에 service 값을 넣어줌

driver.implicitly_wait(3) #3초 기다렸다가 url 가져오기
driver.get(url)

soup = BeautifulSoup(driver.page_source , 'html.parser')
img_list = soup.find_all('div' , class_='KL4Bh')

for img in img_list:
    print(img)
