# 복습 연습 문제
# 정수 3개를 입력받아서 제일 큰 수를 출력하기

# num1 = int(input('정수1 입력 :'))
# num2 = int(input('정수2 입력 :'))
# num3 = int(input('정수3 입력 :'))
#
# if num1>num2 and num1>num3 :
#     print('제일 큰 수 : %d'%num1)
# elif num2>num1 and num2>num3 :
#     print('제일 큰 수 : %d' % num2)
# else :
#     print('제일 큰 수 : %d' % num3)

import numpy as np
shape = int(input('도형 입력(1:사각형 , 2: 삼각형 , 3: 원) :'))
if shape ==1:
    length = int(input('가로입력 :'))
    height = int(input('세로입력 :'))
    print('사각형의 면적 = %.2f'%(length*height))
elif shape == 2:
    length = int(input('밑변 입력 :'))
    height = int(input('높이 입력 :'))
    print('삼각형의 면적 = %.2f' % (length * height*0.5))
elif shape ==3 :
    length = int(input('반지름 입력 :'))
    print('원의 면적 = %.2f' % (length**2 * np.pi))

