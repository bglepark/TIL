# 앞에서 작성한 Dog 클래스에서
# 1. 디폴트 매개 변수를 갖는 생성자를 정의
# 4. 필드 중 breed는 비공개 필드로 정의
# 2. 필드의 값을 가져오고 , 변경하는 메소드를 정의
# 3. sleep() , sit() , run() , eat() 메소드의 내용을 정의
# 잠자기 , 앉다 , 뛰다 , 먹다 등의 내용이 출력되도록 정의

# 인스턴스를 생성하되, 인수의 수를 다양하게 입력하여 생성하는 코드 작성
# 인스턴스를 이용하여 개의 정보를 출력하기
# - 품종 , 나이 , 색상 , 크기 등의 정보를 출력

class Dog:
    def __init__(self , breed='' , size = '' , year=0, color=''):
        self.__breed = breed
        self.size = size
        self.year = year
        self.color = color
        
    def getBreed(self):
        return self.__breed
    
    def setBreed(self,breed):
        self.__breed = breed
        
    def getSize(self):
        return self.size
    
    def setSize(self,size):
        self.size = size
        
    def getYear(self):
        return self.year
    
    def setYear(self,year):
        self.year = year

    def getColor(self):
        return self.color

    def setColor(self , color):
        self.color = color
        
    def sit(self):
        print('앉다')
    
    def eat(self):
        print('먹다')
    
    def run(self):
        print('뛰다')
        
    def sleep(self):
        print('잠자다')


dog1 = Dog('Neapolitan Mastiff' , 'Large' , 5 , 'Black')
dog2 = Dog('Maltese' , 'Small' , 2 , 'White')
dog3 = Dog('Chow Chow' , ' Medium' , 2 , 'Brown')

print(f'dog1의 breed는 {dog1.getBreed()}입니다.')
print(f'dog1의 size는 {dog1.getSize()}입니다.')
print(f'dog1의 year는 {dog1.getSize()}입니다.')
print(f'dog1의 year는 {dog1.getColor()}입니다.\n')

print(f'dog2의 breed는 {dog2.getBreed()}입니다.')
print(f'dog2의 size는 {dog2.getSize()}입니다.')
print(f'dog2의 year는 {dog2.getSize()}입니다.')
print(f'dog2의 year는 {dog2.getColor()}입니다.\n')

print(f'dog3의 breed는 {dog3.getBreed()}입니다.')
print(f'dog3의 size는 {dog3.getSize()}입니다.')
print(f'dog3의 year는 {dog3.getSize()}입니다.')
print(f'dog3의 year는 {dog3.getColor()}입니다.\n')





