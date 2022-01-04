# Literal : 정수 , 실수 , 문자 , 문자열 , 논리값
# 정수 리터럴
''' 여러줄 주석'''
"""여러줄 주석"""

a= 10
b = 0b110001
c = 0o61  #0b110001
d = 0x1f2c #0b0001111100101100
e =0x31

print(a , b , c , d  , e)

# 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 1.234e5

# 문자열 리터럴
str1 = '박현수'
str2 = "Hello"
str3 = """안녕하세요
반갑습니다"""
str4 = '''여러 줄로 나누어
사용할 수 있습니다'''

print(str1 , str2)
print(str3)
print(str4)

# 논리값 리터럴 : True False
t = True
f = False
print(t,f)

# 특수 리터럴 None
name = '이경미'
phone = ''
address = None

print(name, phone , address)
