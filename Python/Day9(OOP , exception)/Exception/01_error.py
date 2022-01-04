# 에러 발생

# 0으로 나눈 경우
# print(10/0) => ZeroDivisionError 발생

# 숫자와 문자열을 같이 사용하여 문자열로 사용하는 에러
# print('나이 : ' + 23 + '살')  => type error
# TypeError: can only concatenate str (not "int") to str

# NameError: name 'b' is not defined
# print(b)


# ValueError: incomplete format
# b=10
# print('%d%'%b)

# SyntaxError: invalid syntax
# b=10
# if b>10   (콜론 사용 안함)
#     print('합격')


# IndexError: list index out of range
# a = [1,2,3,4]
# print(a[4])

# local variable error 가능성
# UnboundLocalError : local variable 'a' referenced before assignment
# def add():
#     a = a+1

# ModuleNotFoundError: No module named 'mymodule'
# import mymodule

# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# f = open('test.txt' , 'r')
# data = f.read()
# f.close()


# OSError: [Errno 22] Invalid argument: 'c:\test.txt'
# \\ => 백슬래시(\) 를 2번 써야함
f = open('c:\test.txt' , 'r')
f.close()

