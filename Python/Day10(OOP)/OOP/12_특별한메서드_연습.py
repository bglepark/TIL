# 앞에서 작성한 dogClass 에서 객체 간의 크기를 비교하는 메서드를 작성
# 1. 객체 간의 크기를 비교하는 메서드를 작성
# 2. 객체 간의 나이를 더하고 , 빼고 , 곱하고 , 나누는 메서드 작성


class Dog:
    def __init__(self, breed='', size='', age=0, color='white'):
        self.__breed= breed
        self.size = size
        self.age = age
        self.color = color

    def getBreed(self):
        return self.__breed

    def setBreed(self, breed):
        self.__breed = breed

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def eat(self):
        print('먹다')

    def sleep(self):
        print('자다')

    def sit(self):
        print('앉다')

    def run(self):
        print('뛰다')

    def printInfo(self):
        info = f'품종 : {self.__breed}\n크기: {self.size}\n나이: {self.age}\n색상: {self.color} '
        print(info)

    def __repr__(self):
        info = f'품종 : {self.__breed}\n크기: {self.size}\n나이: {self.age}\n색상: {self.color} '
        return info

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age

    def __gt__(self, other):
        return self.size < other.size

    def __ge__(self, other):
        return self.size <= other.size

    def __lt__(self, other):
        return self.size > other.size

    def __le__(self, other):
        return self.size >= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __divmod__(self, other):
        return (self.age // other.age, self.age % other.age)


dog1 = Dog('A',"big", 10)
dog2 = Dog('B', 'small', 5)
if dog1 > dog2:
    print('dog1이 dog2 보다 크네요!')
elif dog1 == dog2:
    print('dog1과 dog2는 비슷해요!')
else:
    print('dog2가 dog1 보다 크네요!')

print(dog1)
print(divmod(dog1,dog2))


