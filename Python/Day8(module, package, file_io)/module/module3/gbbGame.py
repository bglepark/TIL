# 가위바위보 게임 모듈

from random import randint
def gbb_game(you_n):
    com_n = randint(1,3)
    if (com_n-you_n) == 1 or (com_n-you_n) == -2:
        print('컴퓨터가 이겼습니다.')
    elif com_n == you_n:
        print('비겼습니다.')
    else :
        print('내가 이겼습니다.')
    print('COM : %d' %com_n)

def input_num():
    you = int(input('YOU입력 (1:가위 , 2:바위, 3:보) : '))
    gbb_game(you)