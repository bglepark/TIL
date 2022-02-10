from bs4 import BeautifulSoup
import urllib.request

#urllib는 내장 모듈 -> request : 요청한다(클라이언트가 서버한테 요청)
# resp : http 객체인데 안에 document가 들어가 있다. -> 응답되는 document를 resp 객체에 담아서 준다
resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver')
# print(resp)

# 어떤걸 가져올건지 / 뭐가 바꿔줄건지
# 파이썬이 가지고 있는 내장 parser로 parse tree를 만들어줬다
soup = BeautifulSoup(resp , 'html.parser')
# print(soup)
# print(type(soup))


# print(soup.a)
#
# print(soup.find_all('a'))
# for i in soup.find_all('a'):
#     title = i.get_text()
#     print(title)


# 제목 찾아보기
# 확인해보면 dl tag 로 뭉텅이 잡혀있고, class 속성으로 잡혀져 있다.
# class : lst_dsc
# findAll 과 find_all 차이 => find_all이 더 최신이다
movies= soup.find_all('dl' , class_ = 'lst_dsc')
# print(movies[0])
for movie in movies:
    #제목 가져오기
    # title = movie.find('a').string
    # title = movie.find('a').text
    # title = movie.find_all('a')[0].get_text()
    title = movie.find('a').get_text()

    # 별점
    star = movie.find('span' ,class_ = 'num').get_text()
    print(f'{title} [{star}]')