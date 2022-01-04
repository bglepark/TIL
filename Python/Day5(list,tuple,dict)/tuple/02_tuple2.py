# 튜플 사용

# 튜플 요소 접근 : indexing
t1 = (10,30,-10,50,100)
print(t1[0] + t1[3])

# 튜플 범위에 접근 : slicing
print(t1[1:3])
print(t1[1:])
print(t1[:])

# 튜플의 덧셈 및 곱셈 연산 : + , *
t2 = ('a' , 'b' , 'c')
print(t1+t2)
print(t2*3)

# 2차원 튜플
tt = ((1,2,3) , (4,5,6) , (7,8,9))
print(tt)
print(tt[0][-1])
print(tt[-1])

myTuple = (10,20,30)
myTuple = list(myTuple)
myTuple.append((40))
print(tuple(myTuple))

# 튜플의 원소 추가하는 방법
# 1) 리스트로 변경한 후 값을 추가하고 다시 튜플로 변경

# 2) + 연산 수행
myTuple = (10,20,30)
update = (40,)
myTuple = myTuple + update
print(myTuple)