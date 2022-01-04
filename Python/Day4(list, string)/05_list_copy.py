# 리스트 복사

# 얕은 복사(shallow copy)
# 실제 리스트가 복사되지 않고 참조값(주소)만 복사
print('shallow copy')
a = [1,2,3,4]
b = a
print(a)
print(b)
a[-1] = 100
print(a)
print(b) #b도 바뀜

# 깊은 복사(deep copy) :
# 리스트 복사본을 새로 생성하여 반환
# list()함수 또는 copy() 함수 사용 / copy 모듈의 deepcopy()
print('deep copy')
c = list(a)
print(c)
c[0] = 'apple'
print(a)
print(c)

d = a.copy()
d[0] = 0.5
print(a)
print(d)

# copy 모듈의 deepcopy 사용
import copy
d = ['a' , 'b' , 'c']
e = copy.deepcopy(d)





