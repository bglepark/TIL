# 수치형 , 문자열 변경 불가능 (immutable)
x= '123'
y= x
y+='4'
print('String')
print(x)
print(y)
print('x id' , id(x))
print('y id' , id(y))


# 튜플은 변경 불가능(immutable)
x = (1,2)
y = x
y += (3,)
print('tuple')
print(x)
print(y)
print('x id' , id(x))
print('y id' , id(y))

# 리스트는 변경 가능(mutable)
x= [1,2]
y=x
y.append(3)
print('list')
print(x)
print(y)
print('x id' , id(x))
print('y id' , id(y))

# 딕셔너리는 변경 가능(mutable)
x = {1:2}
y = x
y[2]=3
print('dictionary')
print(x)
print(y)
print('x id' , id(x))
print('y id' , id(y))
