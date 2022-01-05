# 생성자(constructor)
# : 인스턴스 생성하면서 필드값을 초기화하는 함수

# 생성자를 정의할 때 : __init__()
# 생성자를 호출(사용) = 인스턴스를 만드는것 : 클래스 이름과 같게 사용

# 생성자의 형식
# class Classname:
#     def __init__(self, *args): #*args로 여러 개 인수 사용 가능
#         # 이 부분에 필드를 초기화하는 코드를 입력

# self : 클래스에서 생성된 인스턴스에 접근(인스턴스 자신을 나타냄)
#          인스턴스가 생성된 후 해당 인스턴스 이름으로 값을 할당하거나 메서드 호출
#         클래스 내에서 self 호출
#         생성된 인스턴스 이름과 클래스 내의 self가 같은 역할을 한다
#         메소드를 호출할 때도 인스턴스의 이름과 메서드명을 사용

# _ : 언더스코어 한줄만 쓰면 변수에 특별한 이름을 부여하지 않고 사용하려고 할때
# for i in range(10):
#     print('Hello')
# 
# for _ in range(10):
#     print('Hello')

# __ : 언더스코어 2개 사용 : 특수하게 정의되어 있는 예약함수(메소드), 변수에 사용

# if __init__ == 'main': -> 함수 파트에서 main으로 실행하는 부분


# 기본 생성자 : 생성자에 self만 있고, 다른 매개변수가 없는 경우
# class 클래스명 :
#     def __init__(self):
#         pass

class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'red'

# 인스턴스에서 바로 매소드 사용 가능
car1 = Car()
print(car1.speed)
print(car1.color)


# 매개변수가 있는 생성자
# class 클래스명:
#   def __init__(self, *args) :
#       pass

class Car1:
    def __init__(self , speed , color):
        self.speed = speed
        self.color = color

# 인스턴스 생성 시에 인수를 같이 지정해줘야 한다. -> TypeError 발생
# mycar = Car1()
# print(isinstance(mycar , Car1))

mycar = Car1(10 , 'white') # self 값은 넣어줄 필요가 없다
print(isinstance(mycar , Car1))
print(mycar.color)
print(mycar.speed)

# 디폴트 매개변수를 사용하는 생성자
# class 클래스명:
#   def __init__(self, arg1 = 값1 , arg22 = 값2) :
#       pass

class Car2:
    def __init__(self , speed=0 , color='red'):
        self.speed = speed
        self.color = color

mycar2 = Car2()
yourCar = Car2(10 , 'white')
myCar3 = Car2('Yellow')

print(f'mycar2.color는 {mycar2.color}' )
print(f'mycar2.speed는 {mycar2.speed}')
print(f'yourCar.color는 {yourCar.color}')
print(f'yourCar.speed는 {yourCar.speed}')

print(f'myCar3.color는 {myCar3.color}')
print(f'myCar3.speed는 {myCar3.speed}')
# 이런 경우 color는 default값인 red , 속도가 yellow로 출력된다.
# 인수의 위치를 바꿔야 한다.
# def __init__(self, color='red' , speed=0) default 값을 뒤로 보내야함

class Car3:
    def __init__(self , color= 'red', speed = 0):
        self.speed = speed
        self.color = color

    def drive(self):
        self.speed = 50

    def speedup(self):
        self.speed += 10

# if __init__ == 'main': #(해당 init을 파일 본인에서 사용할 경우!)
myCar4 = Car3()
print('초기 속도' , myCar4.speed)
myCar4.drive()
print('drive()수행 후 속도' , myCar4.speed)
myCar4.speedup()
print('speedup()수행 후 속도' , myCar4.speed)

myCar4.color = 'yellow'




