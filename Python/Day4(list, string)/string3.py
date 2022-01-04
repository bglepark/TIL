# 문자열 쪼개기
# split() : 구분자(공백, 세미콜론 , 콜론, 콤마....)를 기준으로 문자열 나눔
# 리스트로 반환

cities = '인천 대구 대전 부산 울산 청주 춘천'
cities_split = cities.split()
print(cities_split)

names = '성춘향;변학도;이몽룡;방자'
names_split = names.split(';')
print(names_split)

for name in names_split :
    print(name)