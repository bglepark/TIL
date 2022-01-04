# 리스트 연산
# 1. 리스트 합치기 : +
# 2. 리스트 곱하기 : * (반복)
# 3. 리스트 내용 변경

fruits = ['apple' , 'banana' , 'melon']
a = [1,'apple',3.5,[10,20,30],True]

b = fruits + a
print(b)

c = fruits * 3
print(c)

a[3]='melon'
print(a)
a[1:3] = [10,11,12]
print(a)

a[0] = [-1,-4]
print(a)
