# 객체지향프로그래밍 (Object Oriented Programming)
# 함수처럼 어떤 기능을 함수 코드에만 묶어두지 않고 객체에 기능을 정의하는 것
# 함수와 변수를 함께 가지고 있도록 구성
# 코드의 재사용성

# 객체 : 함수(function) + 데이터(변수)

# 예시) TV : 끄다 , 켜다 , 채널을 변경 , 가격

# String

str1 = 'I love you' # 문자열 객체
print(str1)
print(type(str1))
print(str1.split()) # 객체가 할 수 있는 동작 => .split()

# 파이썬은 모든 data를 class(객체) 로 정의함
x = 100
print(type(x))


# 객체 -> 실생활에 존재하는 실제적인 물건 또는 개념
# 예시) 심판 , 선수 , 팀

# 속성 -> 객체가 가지고 있는 변수
# 예시 ) 선수의 이름 ,포지션 , 소속팀

# 행동 -> 객체가 실제로 작동할 수 있는 함수 , 메소드
# 예시 ) 공을 차다 , 패스하다

# 클래스와 인스턴스의 관계
# 붕어빵틀 (클래스)  / 붕어빵 (인스턴스)
# => 클래스(class) => 객체를 만들어내는 틀
                # 객체가 가지는 기본 정보를 담은 코드
# => 인스턴스(instance) => 클래스에서 생성된 객체
#               실제로 생성되는 객체

# 계산기 : 함수와 변수로 동작
result = 0
def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(10))
print(adder(5))

# 계산기가 여러 개 필요할 경우
result1 = 0
def adder1(num):
    global result1
    result1 += num
    return result1

print(adder1(3))
print(adder1(10))
print(adder1(5))

result2 = 0
def adder2(num):
    global result2
    result2 += num
    return result2

print(adder(3))
print(adder2(10))
print(adder2(5))

# => 이렇게 되면 모든 계산기를 생성해주어야 한다
# 클래스로 계산기 정의

class Calculator:
    def __init__(self):  # 초기값을 설정해주는 메소드
        self.result =0 #result값을 0으로 설정

    def adder(self , num):
        self.result += num
        return self.result


cal1 = Calculator()
print(type(cal1))
print(cal1.adder(3))
print(cal1.adder(5))