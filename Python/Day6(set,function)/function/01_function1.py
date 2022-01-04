# 함수 (function) 정의

def show_info():
    print('이름 : 홍길동')
    print('나이 : 20')

show_info()

def welcome(n):
    for i in range(n):
        print('welcome!')

welcome(10)


# 2 개의 숫자를 입력 받아서 합을 구하여 출력하는 함수 작성

# 숫자1 입력 : 10
# 숫자2 입력 : 5
# 10 + 5 = 15

# def sumAB():
#     num1 = int(input('숫자1 입력 : '))
#     num2 = int(input('숫자2 입력 : '))
#     print('%d + %d = %d ' %(num1,num2,num1+num2))
#
# sumAB()

# 반환값을 저장하는 함수 정의
def sumAB():
    num1 = int(input('숫자1 입력 : '))
    num2 = int(input('숫자2 입력 : '))
    return(num1+num2)

# result = sumAB()
# print('합: ', result)


# 반환값을 변수에 저장하지 않고 바로 사용
print('합 :' , sumAB())