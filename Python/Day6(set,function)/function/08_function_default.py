# default 매개변수
# 매개변수의 기본값을 지정

# def greet ( name , msg = 'hello'):
#     print(name +'!'+ msg)
#
# greet('hong' , 'hi')
# greet('hong')


# 디폴트 매개변수는 반드시 마지막에 위치해야 한다!!!!!!!!!!!!!
# def greet ( msg = 'hello' , name):
#     print(name +'!'+ msg)
#
# greet('hi' , 'hong')
# greet('hong')


# 디폴트를 여러개 쓰는 것도 가능하다
def greet (name = 'moo' , msg = 'Hello!!1'):
    print(name+'!'+msg)
greet('henry' , 'nice')
greet('wow')
greet()


# 기본적인 값
# def showInfo(name , year , age):
#     print(name, year , age)
#
# showInfo('홍길동' , 3 , 10)

# 매개변수 디폴트 여러개
def showInfo(name , year = 1 , age = 20):
    print(name, year , age)

showInfo('홍길동' , 3 , 10)
showInfo('홍길동' , 3)
showInfo('홍길동')
