# money = int(input('교환할 돈은 얼마 ? '))
#
# sinsa = money // 50000
# money = (money % 50000)
#
# sejong = money // 10000
# money = (money % 10000)
#
# leelee = money // 5000
# money = (money % 5000)
#
# leehwang = money // 1000
# money = (money % 1000)
#
# hak = money // 500
# money = (money % 500)
#
# baek = money // 100
# money = (money % 100)
#
# oship = money // 50
# money = (money % 50)
#
# ship = money // 10
# money = (money % 10)
#
# print("50000원 %d장 , 10000원 %d장 , 5000원 %d장 , 1000원 %d장" %(sinsa,sejong,leelee,leehwang))
# print("500원 %d개 , 100원 %d개 , 50원 %d개 , 10원 %d개" %(hak, baek , oship , ship))
# print("바꾸지 못한 돈 ==>%d원"%money)
#

# from random import randint
# a_rand = randint(1,6)
# b_rand = randint(1,6)
# print('A의 주사위 숫자는 %d입니다'%a_rand)
# print('B의 주사위 숫자는 %d입니다'%b_rand)
# if a_rand>b_rand:
#     print('A가 이겼다')
# elif b_rand>a_rand:
#     print('B가 이겼다')
# else:
#     print('비겼다')


# for i in range(5,0,-1):
#     print('*' * i)

# for i in range(1,10,2):
#     star = ('*' * i)
#     num = 9
#     star = star.center(num)
#     print(star)
#

# num = 0
# num = int(input('숫자 입력 : '))
# while num != 7 :
#     if num !=7 :
#         num = int(input('다시 입력 : '))
# if num == 7 :
#     print('7 입력! 종료')


price = 2000
balance = 10000
cnt = 0
while balance!=0 :
    cnt +=1
    print('노래를 %d곡 불렀습니다'%cnt)
    balance = balance - price
    if balance == 0 :
        break
    print('현재 %d원 남았습니다'%balance)

print('잔액이 %d원 입니다. 종료합니다.'%balance)
