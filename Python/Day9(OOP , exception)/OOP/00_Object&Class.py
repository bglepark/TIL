# 객체와 클래스

# 예) 계산기
# 3이라는 숫자 입력하고 + 기호 입력한 후 4를 입력
# 계산된 결과값을 어딘가에 저장하고 있어야 함
# 파이썬의 계산기 함수

result = 0
def adder(num):
    global result
    result+=num
    return result

print(adder(3))
print(adder(7))
print(adder(9))
 
 # 결과를 계속 저장하고 있는 result라는 변수가 필요하다
 # 여러 명이 사용하는 계산기가 필요하려면 -> 클래스가 필요하다!

# 계산기 클래스 : Calculator.py
class Calculator:
    def __init__(self):
        self.result = 0
    def adder(self,num):
        self.result+=num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

# 객체 지향 프로그래밍
# 함수처럼 어떤 기능을 함수 코드에 묶어 두는 것이 아니라,
# 객체라고 하는 코드에 그런 기능을 묶은 하나의 단일 프로그램을 넣어 다른 프로그래머가 재사용할 수 있도록 함
# 객체 : 함수와 변수를 함께 가지고 있는 단위
# 컴퓨터 공학의 오래된 프로그래밍 기법 중 하나