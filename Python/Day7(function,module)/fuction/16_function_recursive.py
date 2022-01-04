# # 재귀호출 : 자기함수 호출
#
# # 문제 1. 팩토리얼 계산
# # 3! = 3*2*1  , 0! = 1
# # 반복문을 사용해서 구성
#
# # def factorial(n):
# #     a=1
# #     for i in range(n,0,-1):
# #         a*=i
# #     return a
# #
# # n = int(input('숫자 입력: '))
# # print(f'{n}! = {factorial(n)}')
#
# # fac(n) = n*(n-1)!
# # n! = n*(n-1)!
# # (n-1)! = (n-1)*(n-2)!
# # fac(3) = 3*fac(2)
# # fac(2) = 2*fac(1)
#
# # fac(1) = 1
#
# # fac(n) = n*(n-1)*(n-2)*.....*1
#
#
# # 이게 바로 재귀함수다!!!!!!!!!!!!!!!!! 자기 자신을 되부르기
# # def fac(n):
# #     if n == 1 :
# #         return 1
# #     else:
# #         return n*fac(n-1)
# #
# #
# # print(fac(n))
#
# # 재귀함수는 메모리 공간을 많이 차지해서 자주 사용하지는 않는다
# # 5! ==> fac(5) ==> 5*fac(4) ==> 4*fac(3) ==> 3*fac(2) ==> 2*fac(1) ==>1
# # fac(5) <== 5*4*3*2*1 <== 4*3*2*1 <== 3*2*1 <== 2*1 <== 1
#
# # 주의 : maximum recursion depth exceeded while calling a Python object
# # 다른 예제 -> 무한 오류
# def selfCall():
#     print('hello' , end = ' ')
#     selfCall()
#
# # selfCall()

# count 함수 (1. 반복문 , 2. 재귀함수)
# 반복문 이용
def count(number):
    if number>=1:
        for i in range(number,0,-1):
            print(i)
    else :
        print('1이상인 숫자를 입력하세요')

count(5)

# 재귀함수 이용
# def selfCount(number):
#     if number == 1 :
#         print(1)
#     if number == 0 :
#         print(0)
#     else:
#         print(number)
#         return selfCount(number-1)
# selfCount(5)


# 재귀함수 강사 코드
def selfCount(number):
    if number >= 1:
        print(number)
        selfCount(number-1)
    else:
        return
selfCount(10)