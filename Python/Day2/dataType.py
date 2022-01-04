# 파이썬이 처리하는 자료형 (data type)
# 정수(int), 실수(float), 문자열(str) , 불(bool)

# 정수 : 2진수 , 10진수, 8진수 , 16진수
# 실수 : 3.14 , 1.2e3
# 문자열 : ' ' " "
# 불(논리) : True False

a= 100
b= 3.14
c = 'name'
d= True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 형변환 : int() , float() , str()
# str : 문자열로 변환
print(type(str(100)))
print(str(3.14)+'pie')

str1 = str(3.14)

# int(문자열) : 문자열을 정수형 변환
# float(문자열) : 실수로 변환
num1 = float(str1)
print(type(num1))

# 형변환할때 진수 표기해주기
print(int('1010' , 2))
print(int('1010' , 8))