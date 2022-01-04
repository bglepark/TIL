# 카운트 다운 프로그램
# 시작 숫자를 입력하시오 : 10
# 10 9 8 7 6 5 4 2 1 0 성공

start = int(input('시작 숫자를 입력하시오 : '))

for i in range(start , 0 , -1) :
    print(i , end=' ')
print('성공')