# 앞에서 작성한 car 클래스에서 다음의 두가지 메소드를 추가하시오.
# speedUp(증가할속도량)
# speedDown(감소할 속도량)


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

    def speedUp(self,speed):
        if self.speed >= 140:
            print('과속입니다')
        else:
            self.speed+=speed
        return self.speed

    def speedDown(self,speed):
        if self.speed > 0:
            self.speed-=speed
        else :
            self.speed = 0
            print('정지')

    


car1 = Car('123')
print(car1.speed)
car1.speedUp(20)
print(car1.speed)
car1.speedDown(10)
print(car1.speed)

