# 문자열 슬라이싱(slicing)

crawling = 'Data crawling is fun'
parsing = "Data parsing is also fun"

# indexing
print(crawling)
print(crawling[0])
print(crawling[-1])

# slicing
print(crawling[0:4]) # 0~3번가지의 문자들
print(crawling[17:])
print(crawling[:18])
print(crawling[-1:]) # 마지막에서 끝까지
print(crawling[:-1])
print(crawling[10:10+5])

print(parsing[:])


