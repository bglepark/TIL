# 숫자 10개를 입력 받아서 양, 음 ,0의 개수 출력

plus=0
minus=0
zero =0

for i in range(1,11):
    number = int(input('숫자 %d 입력 :'%i))
    if number>0:
        plus = plus+1
    elif number<0:
        minus = minus+1
    else:
        zero = zero+1
print('-------------------\n')
print('양의 개수 : %d'%plus)
print('음의 개수 : %d'%minus)
print('양의 개수 : %d'%minus)