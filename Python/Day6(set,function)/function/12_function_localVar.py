# 함수 안에서 정의된 변수들은 함수 안에서 국한된다.
# 이러한 변수들을 지역 변수 라고 한다. local 변수(함수 내에서 정의된 변수)
# 함수가 호출되면 생성되고, 함수가 종료되면 지역변수는 소멸

# def show():
#     a=1    # 함수 내부에서 정의된 지역변수
#     print('show() 함수')
#     print(a)

# def show(a):    # a : 매개변수 ==> 함수 내부에서 지역변수로 사용
#     a=a+1
#     print('show() 함수')
#     print(a)
#
# show(10)
# print(a)  # a가 선언된 적이 없어서 오류 발생

# def show():
#     a=1  # a : 지역 변수
#     a = a+1
#     print('show() 함수')
#     print(a)
#
# show()


a=1 # 함수 밖에서 정의된 전역변수 a(global 변수)
def show():
    print('show() 함수')
    print(a)  # 전역변수 a


b = 10
def add():
    print('add() 함수')
    print(a)
    print(b)
    print('-------')


# 전역 변수는 함수 내부에서도 사용이 가능함
show()
add()
print(a)
print(b)
print('------')

# def add2(): # 오류 발생(a에서부터 오류 발생)
#     a = a+1 # 여기서 a는 지역 변수이다 / 연산을 사용했기 때문에 / 그냥 print(a)를 사용하면 전역변수a를 사용
#     c = a+b
#     print('add2() 함수')
#     print(a)
#     print(b)
#     print(c)
#     print('-------')
#
# add2()

# 전역변수 a를 변경하려고 할때
def add2():
    global a #global을 사용하면 전역변수 a를 사용한다 (위에서 a=1로 선언됨)
    a = a+1
    c = a+b
    print('add2() 함수')
    print(a)
    print(b)
    print(c)
    print('-------')

print(a)
add2()
print(a)
# 그냥 print(a)를 썼을때는 a = 1 , add2() 이후엔 a = 2

# 전역 변수는 어디서든지 사용 가능(함수 내부에서도 사용 가능)
# 함수 내부에서 사용하는 지역변수나 매개변수는 함수 내에서만 사용 가능
# 지역변수가 전역변수보다 우선 순위가 높음
# 함수 내부에서 할당연산자 = 사용하는 식에서 변수는 지역변수로 인식
# 함수 내부에서 전역 변수를 변경할 때는 global 키워드를 사용
