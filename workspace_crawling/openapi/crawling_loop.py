from bs4 import BeautifulSoup
import requests

url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5'
resp = requests.get(url)

soup = BeautifulSoup(resp.text , 'html.parser')
#
# titles = soup.find_all('span' , class_='title')
#print(titles)
#
# for title in titles:
#     print(title.text.strip())
#
# numbers = soup.find('nav' , class_='pagination')
# numbers_lst = list()
#
# for number in numbers:
#     numbers_lst.append(number.text)
# numbers_lst.remove('처음 페이지')
# numbers_lst.remove('이전 페이지')
# numbers_lst.remove('다음 페이지')
# numbers_lst.remove('마지막 페이지')
# # print(numbers_lst)
#
# for i in numbers_lst:
#     url='https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage='+i
#     resp = requests.get(url)
#
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     titles = soup.find_all('span', class_='title')
#     # print(titles)
#     print('\n')
#     print(f'{i}번째 페이지')
#
#     for title in titles:
#
#         print(title.text.strip())


paging = soup.find('nav' , class_='pagination')
# nums = list()
# for page in paging:
#     if page.text.isdigit(): #isnumeric으로 가져옴
#         nums.append(page.text)
#
# print(nums)

# 한줄로 만들어보기
# nums = list(filter(None, map(lambda x: x.text if x.text.isdigit() else None, paging )))
# print(nums)


sub_url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage='
nums = list(filter(None, map(lambda x: x.text if x.text.isdigit() else None, paging )))

for i in nums:
    soup = BeautifulSoup(requests.get(sub_url+i).text , 'html.parser')
    titles = soup.select('span[class=title]')
    for title in titles:
        print(title.text.strip())