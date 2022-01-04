# Set : 집합 형태의 자료 구조 (집합 자료형)

s1 = {1,2,3,4,5}
s2 = set([3,4,7,8,9])
s3 = set()

print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
# print(dir(s1))
print(type(s3))

# set 의 특징
# 1. 중복을 허용하지 않음 : unhashable type
# 2. 순서가 없음 -> 입력 순서와 출력되는 순서가 다를 수 있음
s4 = {1,3,2,2,5,4,3}
print(s4)

# 3. 인덱스 사용 불가 : 이미 포함되어 있는 요소를 변경할 수 없음

# print(s4[0]) => type error 발생

# 4. 추가 : add , update

# 1개 추가 :  add()
s4.add(10)
print(s4)
# 여러개 추가 : update()
s4.update([5,6])
print(s4)

# 5. 집합 안에 변경가능한 항목 포함 불가능
#   : 리스트 포함 불가 , 튜플 포함 가능

# s5 = {1,2, [3,4]}
s6 = {1,2, (3,4)}
print(s6)

# 6. 요소 삭제 가능

# remove 기능
# s1.remove(1)
# print(s6)
# remove는 없는 값에 대해서 keyerror 발생

# discard 기능
# s6.discard(1)
# print(s6)
# 요소 값이 없는 경우 에러 없음

# 요소 전체를 지움 => 빈집합 => 집합 자체는 존재함
s6.clear()
print(s6)

# 요소 뿐만 아니라 변수 자체도 다 지움! : del
# del s6




