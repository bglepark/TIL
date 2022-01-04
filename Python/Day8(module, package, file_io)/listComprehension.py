# list comprehension
# 리스트를 빠르게, 간결하게 처리 : 파이썬 코드 스타일

# 예시) 정수 0~9까지의 값을 갖는 리스트를 생성하시오.

result = []
for i in range(10):
    result.append(i)
print(result)

# list comprehension : for문을 list안에 사용
result2 = [i for i in range(10)]
print(result2)

# 예시) 짝수만 리스트로 생성 : 필터링
result3 = []
for i in range(10):
    if i%2 == 0:
        result3.append(i)
print(result3)

# list comprehension : 리스트 요소 필터링
result4 = [i for i in range(10) if i%2 ==0]
print(result4)

result5 = [i if i%2 ==0 else 10 for i in range(10)]
print(result5)

# list comprehension : 중첩 반복문
list1 = ['a' , 'b' , 'c']
list2 = ['D' , 'E' , 'F']
result =[]

for i in list1:
    for j in list2:
        result.append(i+j)
print(result)

result2 = [i+j for i in list1 for j in list2]
print(result2)

result2 = [i+j for i in list1 for j in list2 if not(i==j)]
print(result2)


words = 'Remember to let her into your heart'.split()
print(words)

result = [[w.upper() , w.lower() , len(w)] for w in words]
print(result)