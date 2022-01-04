# 문자열에서 사용되는 연산 함수들 (메소드)

# len() : 문자열 길이 반환
string = 'programming'
print(len(string))

# .count() : 문자열 내에 들어있는 특정 문자(열)의 개수 반환
print(string.count('r'))
print(string.count('m'))
print(string.count('ing'))

# .find(찾을문자[위치를 반환])
# .find(찾을문자 [ . start [,end]])
crawling = 'Data crawling is fun'
print(crawling.find('is')) # 찾으면 인덱스 반환
print(crawling.find('parsing')) # 찾는 문자열이 없는 경우 -1 반환
print(crawling.find('is',15))
print(crawling.find('is',5,18))

# .index(찾을문자[, start [,end]])
# 문자열 내에서 특정문자열의 시작 위치를 반환
# 찾는 문자열이 없으면 에러를 반환
print(crawling.index('is')) # 찾으면 인덱스 반환
# print(crawling.index('parsing')) # 찾는 문자열이 없는 경우 -1 반환
