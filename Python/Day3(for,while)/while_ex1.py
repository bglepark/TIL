# 'stop' 문자 입력될때까지 숫자를 입력하고, 입력된 숫자의 개수를 출력

# num = input('숫자 입력 : ')
# cnt = 0
# while num !='stop':
#     num = int(num)
#     cnt +=1
#     num = input('숫자 입력 : ')
#     print(num)
# print('숫자 개수 : ', cnt)


# 7을 입력할때까지 계속 입력
num = 0
while num != 7 :
    num = int(input('숫자 입력 : '))
if num == 7 :
    print('7 입력! 종료')
    
# 무한루프
while True : 
    num = int(input('숫자입력:'))
    if num == 7:
        break
print('입력 종료')