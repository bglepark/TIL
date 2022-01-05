# 인스턴스(instance) 변수 : 필드

# 클래스 변수 : 여러 인스턴스가 공유하는 변수
class Car:
    color = '' # 클래스 변수들이다.
    speed = 10
    count = 0
    
    def __init__(self):
        self.speed = 0 # 인스턴스에 해당하는 부분이 된다
        Car.count += 1 #클래스 이름을 사용함 -> 공용으로 사용
        print(f'현재 총 {Car.count}대가 생산되었습니다.')

car1 = Car()
print(car1.count)
car2 = Car()
print(car1.count)
print(car2.count)

print(Car.count)  # 보통 클래스 이름의 메소드로 사용함

car1.speed # 인스턴스 변수 : 필드
car2.speed


