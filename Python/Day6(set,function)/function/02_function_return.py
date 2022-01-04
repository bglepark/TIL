# 반환값

# 문제1. 사각형의 넓이 계산하는 함수 getArea()
# 매개변수(parameter) : 가로(width) , 세로(height)
# 넓이를 반환

def getArea(width , height):
    area = width*height
    return area

getArea(10,20)
print(getArea(10,20))

# 문제1. 사각형의 넓이 계산하는 함수 getArea()
# 가로와 세로의 길이를 입력받기
# 넓이를 반환

def getArea2():
    width = int(input('가로길이:'))
    height = int(input('세로길이:'))
    result = width*height
    print(f'가로 : {width}, 세로 : {height}, 사각형넓이 = {result}')
    return result

# getArea2()


# 반환값이 여러 개인 경우 (반환된 여러 개를 하나에 받기)
# def multi_return():
#     return 1,2,3
#
# result = multi_return()
# print(result)
# print(type(result)) # 튜플 형식으로 반환 (일반적으로 숫자만 입력해서 반환할 경우)
# print(type(multi_return()))
#
#
# # 반환된 여러 개의 값을 여러 변수로 각각 받기
# a , b , c = multi_return()
# print(a)
# print(type(a))

# return 문이 여러개 사용할 경우 : 가장 첫번째 return 문장만 실행
# return : 값을 반환하고 함수 종료
def multi_return():
    return 1
    return 2
    return 3

result = multi_return()
print(result)