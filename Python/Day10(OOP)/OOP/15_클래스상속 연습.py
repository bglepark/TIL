# 클래스 상속과 메서드 재 정의 연습

# Animal 클래스 정의
# talk() 메소드 정의
# eat() 메소드 정의
# sleep() 메소드 정의
# 필드 : age , leg , color , breed

# 서브클래스 Dog 클래스
# 메소드 : talk() 재정의 -> 멍멍

# 서브클래스 Cat 클래스
# 메소드 : talk() 재정의 -> 야옹

class Animal :
    age = 0
    leg = 0
    color = ''
    breed = ''
    count = 0

    def __init__(self , age , leg , color , breed):
        self.age = age
        self.leg = leg
        self.color = color
        self.breed = breed
        Animal.count +=1
        print(f'현재 {Animal.count}마리의 동물이 있습니다.')
        print(f'동물은 {self.breed}입니다.')


    def talk(self , word):
        print(f'{word}라고 말합니다.')

    def sleep(self , place):
        print(f'{place}에서 잠을 잡니다.')

    def eat(self , food):
        print(f'{food}를 주로 먹습니다.')

class Dog(Animal):
    def __init__(self , age , leg , color , breed) :
        super().__init__(age, leg , color , breed)

    def talk(self, word='멍멍'):
        print(f'{word} 이라고 말합니다.')

        def sleep(self, place):
            print(f'{place}에서 잠을 잡니다.')

        def eat(self, food):
            print(f'{food}를 주로 먹습니다.')
            
class Cat(Animal):
    def __init__(self , age , leg , color , breed) :
        super().__init__(age, leg , color , breed)

    def talk(self, word='야옹'):
        print(f'{word} 이라고 말합니다.')

        def sleep(self, place):
            print(f'{place}에서 잠을 잡니다.')

        def eat(self, food):
            print(f'{food}를 주로 먹습니다.')

animal1 = Animal(10, 0 , 'navy' , 'Dolphin')
animal1.sleep('house')
animal1.eat('fish')
animal1.talk('Strange')
print('\n')

dog1 = Dog(3,4, 'brown' , 'poodle')
dog1.sleep('cage')
dog1.eat('meat')
dog1.talk()
print('\n')

cat1 = Cat(2,4,'white' , '고양이')
cat1.sleep('sofa')
cat1.eat('snack')
cat1.talk()

# 다형성(polymorphism) : 같은 이름의 메서드가 서로 다른 기능을 할 수 있게 만든 것
animals = [Cat(1,4,'s' , 'a'),Cat(1,4,'s' , 'b'),Dog(1,3,'s' , 'a')]

for animal in animals:
    animal.talk()




