# 리스트의 요소 제거

# remove(값)
# 무조건 처음으로 만나는 값을 제거한다

# pop() : 무조건 마지막의 요소 값을 제거
# pop(index) : 해당하는 index 위치의 값을 제거

x = ['apple' , 'banana' , 'coconut' , 'melon' , 'banana' , 'apple']
print(x)
x.remove('melon')
print(x)
# x.remove('banana')
# print(x)

n = x.count('banana')
print(n)

for i in range(n):
    x.remove('banana')
print(x)

y = [1,3,5,1,10]
last = y.pop()
print(y)
print(last)
y.append(-10)
print(y)
rm = y.pop(3)
print(y)
print(rm)

# y.remove(0) -> 제거하려는 값이 없으면 오류 발생
y[3] ='list'
print(y)

y.pop()
print(y)
y.pop()
print(y)
y.pop()
print(y)
y.pop()
print(y)
y.pop()
print(y)
