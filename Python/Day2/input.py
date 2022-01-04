# 입력 함수 : input ()
# 키보드로부터 값을 입력 받아서 처리하기 위해서
# 입력 함수를 수행한 결과 반환된 데이터 유형은 문자열

#x = 100
#y = 300

#print(x+y)

name = input('이름: ')
age = input('나이: ')

print('이름은 %s이고, 나이는 %d입니다' %(name , int(age)))

#print(name)
#print(age)

print(type(name))
print(type(age))
