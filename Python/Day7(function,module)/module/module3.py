# 직접 만든 모듈 사용하기

import calculator

if __name__ =='__main__':
    print('module3.py')
    print(calculator.add(10,3))
else:
    print('sub')
    print(calculator.add(10,3))
# 
# print(calculator.add(10,3))
# print(calculator.sub(10,3))
# print(calculator.mod(10,3))
# print(calculator.mul(10,3))
# print(calculator.div(10,3))

# from calculator import add , sub
# # 모듈명을 사용하지 않고 바로 함수 이름을 사용
# print(add(10,3))
# # print(div(10,3)) # 불러오지 않은 함수는 사용 불가능

from calculator import *
# 전부 다 불러오기


# # 별칭으로 사용
# import calculator as cal
# print(cal.add(10,3))
