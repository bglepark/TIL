# 필드 이용 메소드

class Car:
    model = '' 
    
    def __init__(self, speed , color , model):
        self.speed = speed
        self.color = color
        self.mode = model
     
    # 필드값을 반환하는 메소드   
    def getModel(self):
        return self.model #클래스 안에 있는 전역 변수 model 값을 반환
    
    # 필드값을 변경하는 메소드
    def setModel(self , model):
        self.model = model

    # 필드값을 반환하는 메소드 2
    def getSpeed(self):
        return self.speed

    # 필드값을 변경하는 메소드 2
    def setSpeed(self, speed):
        self.speed = speed

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

        
myCar  = Car(0,'red','아우디')
print(myCar.getColor())
myCar.setModel('벤츠')
print(myCar.getModel())
myCar.getSpeed()
myCar.getModel()