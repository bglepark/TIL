# 1. 클래스 선언
# 클래스 이름 : 식별자 규칙에 정의, 대문자로 시작(구분하기 위해서 대문자로 시작)
# 필드가 없는데 instance를 생성한 후에 필드를 추가하는 과정 => __init__ 사용 x
class Car :

    def speedUp(self):
        pass

    def speedDown(self):
        pass



# 2. 객체(인스턴스) 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
# 필드가 없는데 instance를 생성한 후에 필드를 추가하는 과정
myCar.color = 'black'
myCar.speed = 0

print(myCar.color)
