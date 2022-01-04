# 튜플 : tuple
# 원소 추가, 삭제, 변경 불가

# 튜플 생성 : () , tuple()

t1 = (1,2,3)
print(t1)
print(type(t1))

t2 = 4,5,6
print(type(t2))

t3 = tuple([1,2,3])
print(t3)

t4 = [1,2] , [3,4]
print(t4)
print(type(t4[0]))
# t4[0] = [-1]   튜플은 변경 불가
# 튜플 인덱스로 접근해서 변경 불가 : assignment 불가

# 튜플의 요소를 변경 불가 : 리스트로 변환하여 변경 가능
to_list1 = list(t4)
print(to_list1)
to_list1[1] = 10

t4 = tuple(to_list1)
print(t4)

# 튜플 다루기 : 요소의 위치 index , 일치 항목의 개수 count()

print(t2.index(5))
print(t2.count(4))

# 튜플 삭제 : del()
del(t1)
print(t1)
