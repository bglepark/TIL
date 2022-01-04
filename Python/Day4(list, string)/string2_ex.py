# 도시명을 입력하고 해당 도시가 있는지 유무를 출력하기

cities = '인천 대구 대전 부산 울산 청주 춘천'
city = input('도시명을 입력하세요 : ')

if city in cities :
    print('해당 도시가 있습니다')
else :
    print('해당 도시가 없습니다')

# find() 이용할 경우
cities = '인천 대구 대전 부산 울산 청주 춘천'
city = input('도시명을 입력하세요 : ')
if cities.find(city)!=-1 :
    print('정답')
else :
    print('오답')