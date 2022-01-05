# class Dog :
#     def __init__(self):
#         self.Breed = ''
#         self.Size = ''
#         self.Age = ''
#         self.Color = ''
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def sit(self):
#         pass
#
#     def run(self):
#         pass
#
#
# nm = Dog()
# mal = Dog()
# chow = Dog()
#
# nm.Breed = 'Neapolitan Mastiff'
# nm.Size = 'Large'
# nm.Age = '5 years'
# nm.Color = 'Black'
#
# mal.Breed = 'Maltese'
# mal.Size = 'Small'
# mal.Age = '2 years'
# mal.Color = 'White'
#
# chow.Breed = 'Chow Chow'
# chow.Size = 'Medium'
# chow.Age = '3 years'
# chow.Color = 'Brown'
#

# 강사 코드
class Dog:
    breed =''
    size=''
    age=0
    color='white'

    def eat(self):
        pass
    def sleep(self):
        pass
    def sit(self):
        pass
    def run(self):
        pass

dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

dog1.age = 10
dog2.sleep()

# 다음과 같이 __init__을 사용해도 가능
# def __init__(self):
    # 해당 클래스에서 인스턴스를 만들때(생성자를 정의)
    # self.breed = ''
    # self.size = ''
    # self.age = 0
    # self.color = 'white'
