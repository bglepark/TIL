# 리스트 :
# 집합적 자료형 - 여러 개의 원소를 가지는 데이터
# 가변적 - 삽입 , 삭제 , 변경
# 다양한 형식의 데이터 : 숫자, 문자열, 논리형
# 리스트 : [ ]

# 리스트 생성
list1 = []
print(list1)
print(type(list1))

list2 = list()
print(list2)
print(type(list2))

list3 = [1, 2, 3]
print(list3)

list4 = [1, 'apple' , 3.5 , [10,20,30], True]
print(list4)

# 리스트 요소 출력
for l in list4 :
    print(l , end = ' : ')
    print(type(l))
print()

# 리스트의 길이 : len(리스트 이름)
# 리스트 인덱싱 : 리스트의 인덱스를 이용하여 접근 : 리스트명[indexId]

print('문자열의 길이 : ', len(list4))
for i in range(0, len(list4)):
    print(list4[i], end=' : ')
    print(type(list4[i]))

# 리스트의 각각의 값은 변수에 저장
nums = [1,2,3]
a,b,c = nums
print(a)
print(b)
print(c)
