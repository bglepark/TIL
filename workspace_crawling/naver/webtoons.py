# -*- coding:utf-8 -*-

# 해당 파일은 utf-8로 encoding 됩니다 -> 주석 안에 써야 적용된다

from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url)
# print(resp)
# print(resp.text)
# resp.text : 문자열로 출력된다

soup = BeautifulSoup(resp.text , 'html.parser')
# print(soup)
# 이번에는 BeautifulSoup 객체로 출력된다

# webtoons = soup.find('ul' , class_='img_list')
webtoons = soup.find('ul' , {'class' : 'img_list'})
# print(webtoons)

dl_list = webtoons.select('dl')
# select는 css 표현식으로 지정해주면 그것을 가지고 온다 / css 선택자이다

lst = list()
for dl in dl_list:
    title = dl.find('a')['title'] #a태그 안의 title의 속성값을 가져옴 / 웹툰 제목이 긴 경우에는 ...으로 표기 되기 때문에 title 속성값
    star = dl.find('strong').text

    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star

    lst.append(tmp)

# print(lst)
res = dict()
res['webtoons'] = lst
# print(res)
# json 형태의 문자열로 구성해놨다 => 중괄호 안에 value

res_json = json.dumps(res ,ensure_ascii=False) #ensure_ascii=False : ascii code를 그냥 한글로 만들기
print(res_json)

with open('webtoons.json' , 'w' , encoding='utf-8') as f:
    f.write(res_json)








