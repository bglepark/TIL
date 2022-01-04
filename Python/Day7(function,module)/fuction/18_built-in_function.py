# 내장함수(built-in functions)
# 파이썬에 이미 만들어져 내장되어 있는 함수들
# 별도의 모듈을 import 하지 않고 사용가능

# 함수의 형식과 목적에 따라 호출해서 사용
# print() , input() , id() , type() , sum() , int() , str() , list() , len()
# 특정 객체를 통해 사용 가능한 함수(메소드)
# 리스트.index() , append() , insert() , count() , remove() ....
# 문자열.index() , find() , sort() , reverse() ,....

# https://docs.python.org/ko/3.9/library/functions.html

# abs() : 절대값 계산
print('abs() ---')
print(abs(-10.5))

# all() : 모든 요소가 참이면 True
# False : 0인 경우 , True : 0이 아닌 값
# Iterable(반복 가능한 자료형) : 리스트 , 튜플 , 딕셔너리
# for 반복문을 이용해서
print(all([1,2,3,4]))
print(all([0,1,2]))

# any() : 하나라도 참이면 True
print('any() ------')
print(any([1,2,3,4]))
print(any([0,1,2]))
print(any([0,0,0]))
print(any([0,"",1])) # 빈 문자열 "" : False로 인식
print(any([0,"",0]))
print(any([0,"",0, []])) # 빈 리스트[] : False로 인식

# bool() : bool 값으로 변환 , True / False
print(bool(""))
print(bool([]))
print(bool(1))
print(bool(10))
print(bool(-1))
print(bool({}))
print(bool(None))

# chr() : 아스키코드(ASCII) 값에 해당하는 문자 반환
print("chr()------")
print(chr(95))
print(chr(97))
print(chr(65))
print(chr(48))


# ord() : 문자에 대한 ASCII 코드 값 반환
print(ord("A"))
print(ord("a"))
print(ord(' '))
print(ord("\n"))
print(ord("\t"))
print(ord("0"))

# divmod(a,b) : a를 b로 나눈 몫과 나머지 반환
print("divmod()---------")
print(divmod(10,3)) # 반환 값은 튜플 형태 (몫, 나머지)

# enumerate() : 시퀀스의 각 값에 인덱스를 포함해서 enumerate 객체로 반환
# 시퀀스 : range() , 문자열 , 리스트, 튜플
print("enumerate() -------")
print(enumerate('hello'))
for i , c in enumerate("hello"):
    print(i,c)

for i , season in enumerate(['봄' , '여름' , '가을' , '겨울']):
    print(i,season)


# eval() : 표현식의 연산 결과 반환
print("eval()--------")
print(eval('1+2'))
print(eval('3*4'))
print(type(eval('10'))) # 숫자형으로 나옴
x=1
print(eval('x+1'))

# filter() : 걸러내다
# filter(function , iterable) : iterable 자료의 요소들을 function으로 필터링한다.
print("filter()--------")

def positive(x):
    return x>0

print(filter(positive, [0,1,-1,10,-3,5])) # 함수 이름만 사용
# positive 함수로 걸러낸 객체 변환
print(list(filter(positive, [0,1,-1,10,-3,5])))

def even(x):
    if x%2==0:
        return x
print(list(filter(even , [0,1,-1,10,-3,5])))

# help() : 도움말
help(print)
help(filter)
help(input)
help(max)

# pow(x,y) : x의 y승
print(pow(10,3))
print(pow(2,10))

# range([start] , stop , [,step]) : 지정한 범위의 값을 반복 가능한 객체로 반환
print(range(0,5))
print(list(range(0,5)))
print(list(range(10,1,-1)))

# map() 함수 : 리스트나 튜플, 문자열 등 반복가능한 구조의 요소별로 지정된 함수
# 원본은 변경하지 않고 list , tuple 형태로 반환
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

# 문제. 정수형으로 바꾸기
number1 = [3.5 , 3.4 , 2.0 , 4.6]

# # map 이용
# integer1 = list(map(lambda number:int(round(number)),number1))
# print(integer1)
#
# # for 이용
# def integer2(number):
#     return int(round(number))
# for i in range(len(number1)):
#     number1[i]=integer2(number1[i])
# print(number1)
#
# # 강사 코드
# # for 이용
# result = []
# for i in range(len(number1)):
#     result.append(int(number1[i]))
# print(number1)

# map 사용
print(list(map(int, number1))) # int라는 함수가 있으니까 굳이 안만들고 바로 사용
print(number1)

# zip() : iterable 에서 동일한 인덱스 요소를 추출하여 묶어서 반환
print(zip([1,2,3] , [4,5,6])) # zip 객체로 출력됨
print(list(zip([1,2,3] , [4,5,6])))

print(list(zip([1,2,3] , [4,5,6] , [7,8,9]))) # 반환되는 형태가 tuple 형태로 나옴

keys = ['apple' , 'melonm' ,'banana']
vals = [250 , 300 , 400]
print(list(zip(keys, vals)))
print(dict(zip(keys, vals))) #딕셔너리 형태로 출력

keys = ['apple' , 'melonm' ,'banana']
vals = (250 , 300 , 400)
print(list(zip(keys, vals))) #서로 다른 자료형도 가능