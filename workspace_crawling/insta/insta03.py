from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id 입력 : ')
input_pw= input('pw 입력 : ')

service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.instagram.com/accounts/login/')
sleep(5)

# id = driver.find_element_by_id()
# 사용하지 마세요

# id = driver.find_element(By.NAME , 'username')
id = driver.find_element(By.NAME , 'username')
id.send_keys(input_id)

pw = driver.find_element(By.NAME , "password")
pw.send_keys(input_pw)
sleep(2)

# form 태그 안에 div 태그 안에 3번째 div
driver.find_element(By.CSS_SELECTOR , "#loginForm > div > div:nth-child(3)").click()
# sleep(2)
# driver.refresh()
# 로그인 버튼이 안눌리는경우 새로고침

sleep(3)
later = driver.find_element(By.XPATH , '/html/body/div[1]/section/main/div/div/div/div/button')
# XPATH : 절대경로
later.click()

sleep(3)
later2 = driver.find_element(By.XPATH , '/html/body/div[5]/div/div/div/div[3]/button[2]')
later2.click()