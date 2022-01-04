# 위치 인수와 키워드 인수


def sumN(a,b,c):
    print('a: ' , a)
    print('b: ' , b)
    print('c: ' , c)
    return a+b+c

#위치에 의해 인수를 구별하는 방식 : 기본
print(sumN(10, 20, 30))

# 위치가 달라도 인수값을 정확히 지정해주면 가능
print(sumN(a=10 , c=30 , b=20))
print(sumN(c=20 , b=50 , a=-10))
# 하나라도 키워드 형태로 주면 다른 값도 다 키워드 형태로 값을 주어야 한다.