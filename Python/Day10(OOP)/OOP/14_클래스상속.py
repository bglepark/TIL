# 클래스상속
# 상속을 해주는 클래스 : 부모 클래스
# 상속을 받는 클래스 : 자식 클래스 , 자손 클래스
# 상위 클래스인 자동차 클래스를 슈퍼클래스 또는 부모 클래스 , 하위의 승용차와 트럭 클래스는 서브 클래스 또는 자식 클래스
# 공통된 내용ㅇ르 자동차 클래스에 놓고 상속을 받음

# 상속 구현 문법
# class 서브_클래스(슈퍼_클래스):

# 자동차 클래스 예시
class Car :
    speed = 0
    color = ''

    def __init__(self , speed , color):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}로 주행합니다.')

class Truck(Car):
    def __init__(self, speed , color , load):
        super().__init__(speed , color) #부모 객체의 메소드를 그대로 물려받음 : super()
        self.load = load

    def drive(self):
        print(f'{self.speed}로 {self.load}양의 짐을 싣고 주행합니다.')

    def loading(self):
        print(f'최대 {self.load}의 양을 짐을 운반할 수 있는 트럭')

truck1 = Truck(10, 'red' , 1000)
truck1.drive()
truck1.loading()

# 서브클래스 vehicle : seat
# 승용차 클래스 vehicle : seat

class p_Car(Car):
    def __init__(self, speed , color , people_n):
        super().__init__(speed, color)
        self.people_n = people_n

        # 메서드 재 정의 ! (오버라이딩)
        def drive(self):
            print(f'{self.speed}로 {self.people_n}인의 사람이 타고 주행합니다.')

p_car1 = p_Car(10 , 'black' , 5)
p_car1.drive()

