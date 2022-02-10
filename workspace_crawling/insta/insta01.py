from bs4 import BeautifulSoup
import requests
tag = input('search tages: ')
url = f'https://www.instagram.com/explore/tags/{tag}'
resp = requests.get(url)
soup = BeautifulSoup(resp.text , 'html.parser')
# print(soup)

#KL4Bh

print(soup.find('div' ,class_='KL4BH'))

# javascript 에서 onload=function() 하면 body에 있는 내용들이 화면에 다 그려진 이후에 동작함
# 사이트에서 화면을 줄였을때 반응하는게 반응형 웹이다
# 큰 틀만 보내주고 ajax로 처리한다
# react.js => facebook이 만듦 , instagram은 facebook이 만듬
# react => CSR이다 : 클라이언트에서 화면을 렌더링해준다 -> 그래서 그냥 soup.find를 하면 None이 표기된다