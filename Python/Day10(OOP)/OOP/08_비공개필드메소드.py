# 비공개 필드와 메소드 생성 & 이용

# 비공개 필드 : 필드를 외부에서 직접 사용하지 못하게 하는 방법
#           클래스 내부에서만 사용 가능
# __필드명 : 언더스코어 __ 2개 사용
# 형식 : __필드명

# 비공개 메소드 : 외부에서 직접 사용하지 못하고 클래스 내부에서만 접근
# 형식 : def __메소드명(self,*args)

class Car :
    def __init__(self , modelN, speed=0 , color = 'white'):
        self.modelN = modelN
        self.speed = speed
        self.__color = color # 클래스 내에서만 사용하는 비공개 필드

    def __modelN(self):
        print(self.modelN)

    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color = color

    def printInfo(self):
        self.__modelN()
        print(self.getColor())

# 비공개 필드를 접근하려면 필드를 이용하는 메소드를 정의하여 호출
car1 = Car('1234-454')
# print(car1.color) # 사용할 수 없다.
print(car1.getColor())
car1.setColor('red')
print(car1.getColor())
car1.printInfo()