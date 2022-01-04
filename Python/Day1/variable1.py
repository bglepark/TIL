# 2021-12-20 변수
# 1) 레퍼런스 : 값(객체)이 저장된 메모리의 위치를 가리키는
#     레퍼런스(reference : 참조)
# 2) 동적 타이핑 : 값의 형에 따라서 고정되지 않고,
#     동적으로 자료 유형을 매핑해서 사용
#    type 검사 (자료형이 지정되어 있지 않다)
# 3) 변수는 이름을 가지고 있다.
# 4) 변수는 다른 값을 저장할 수 있다(값 변경 가능)
# 5) 변수는 선언이 필요없다.

# 자바 : int x
#       x = 100.0 (오류)

x = 10
print(x)
id(x)  # 변수가 가리키는 값(객체)의 주소
type(x) # 변수가 가리키는 값의 형식

y = 'hello'
print(y)
y = 'haha'
print(y)
y = 100
print(y)
y = 10.5

y = [10, 30, 40]
id(y)
type(y)

z = y

# 변수 이름
# 1) 대소문자 구분 : C언어 기반
#     X, x
# 2) 영문자, 숫자, 밑줄(_)
#    x1 (ok)
#    1x (error)
# 3) 중간에 공백 X
#     snake : std_name
#     camel : stdName
# 4) 예약어는 변수명을 사용할 수 없다

import keyword
keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

len(keyword.kwlist)
# 35


# 변수에 값 저장 : 할당(assign)
# 변수 = 값
a = 100

# 변수1, 변수2, 변수3 = 값1, 값2, 값3
a,b,c=1,2,3

# 변수1 = 변수2 = 변수3 = 값1
a = b = c = 100

# 변수값 교환(swap)
a, b = b, a

# 변수 삭제: del 변수명
del z


# 연습문제1 : 자신의 이름과 나이를 변수에 저장한 후,
# print()를 이용하여 한 줄에 출력하시오.
# 이름은 문자열로, 나이는 숫자로 저장

name = '이경미'
age = 20

# name, age = '이경미', 20
# print(name + ' ' +str(age))
# print('나는 ' + name + ' 나이는 ' +str(age))
print(name, age)

name='이성길'
age=27
print('이름:{},나이:{}'.format(name, age))
print('성명 : %s, 나이 : %d' %(name, age))


print(f'{name} {age}')


# 연습문제2.
# 변수 선언 후 값 저장하여 출력
# 변수 : name, no, year, grade, average
# 출력 형식
# 성명 : 홍길동
# 학번 : 2016001
# 학년 : 4
# 학점 : A
# 평균 : 93.5

name,no,year,grade,average='김영진',2021012,4,'A',93.5
print('성명 : '+name)
print('학번 : '+str(no))
print('학년 : '+str(year))
print('학점 : '+grade)
print('평균 : '+str(average))

name,no,year,grade,average='김영진',2021012,4,'A',93.5
print('성명 :', name)
print('학번 :', no)
print('학년 :', year)
print('학점 :', grade)
print('평균 :' ,average)


# -----------------
# 포맷 코드 사용

# 형식 : print('서식' % 값)
# 형식 : print('문자열 %d 문자열' % 변수)
# 서식 : %d %f %s %o %x %%

name='이성길'
age=27
print('나이 : %d살' % age)
print('이름 : %s' % name)


name, no, year, grade, average = '이유진', 1234, 4, 'A+', 100
print('성명 : %s\n학번 : %d\n학년 : %d\n학점 : %s\n평균 : %d' %(name ,no,year,grade,average))

print('성명 : %s' % name)
print('학번 : %d' % no)
print('성명 : %s, 나이 : %d' %(name, age))
rate = 80
print()