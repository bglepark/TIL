# list의 정렬 : sort() , reverse()
# sorted(리스트) => 정렬해서 새로운 리스트로 만들어줌 , 원본 리스트는 변경하지 않음
# .sort() : 오름차순 정렬
# .sort(reverse=True) : 내림차순
# .reverse() : 원래 리스트의 순서를 역순서로 변경

scores = [90,78,81,64,99]
print('정렬 전 : ' , scores)
scores.sort()
print('정렬 후 : ' , scores)

scores = [90,78,81,64,99]
scores.sort(reverse=True)
print('내림차순 정렬 후 : ' , scores)

scores = [90,78,81,64,99]
scores.reverse()
print('reverse() 적용 후 : ' , scores)

scores = [90,78,81,64,99]
result = sorted(scores)
print(scores)
print(result)


# .sort(key = )

chr = ['b' , 'A' , 'e' , 'C']
print(chr)
chr.sort()  #알파벳 대문자 먼저
print(chr)

# 대소문자 구별없이 일반적으로 정렬
chr = ['b' , 'A' , 'e' , 'C']
print(chr)
chr.sort(key=str.lower) #일반적으로 정렬하는 것과 같다
print(chr)

chr.sort(key=str.lower , reverse=True)
print(chr)


