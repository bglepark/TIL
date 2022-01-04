# 딕셔너리 : 키와 값의 쌍으로 이루어진 데이터
# {키1:값1 , 키2:값2 , ....}

# 딕셔너리 생성 : {} or dict()


students = {1:'최선' , 2:'홍길동' , 3:'강감찬'}
print(students)
print(type(students))

prof = {}
print(prof)
prof[1] = '이순신'
prof[2] = '홍길동'
print(prof)

print(students[1])

# 중복된 key는 사용 불가능 , value값으로 호출 불가능
member = {'name':'홍길동' , 'phone':'010-1234-1234'}
print(member['name'])

naver = {'name' : 'naver' , 'url':'www.naver.com' , 'id':'hspark'}
google = {'name' : 'google' , 'url':'www.google.com' , 'id':'hspark'}
daum= {'name' : 'daum' , 'url':'www.daum.com' , 'id':'hspark'}

print(naver['name'])
naver['id']='idValue'
print(naver['id'])


# keys() , values() , items()
# 리스트 형태로 출력됨
print(naver.keys())
print(naver.values())
print(naver.items()) #튜플 형태로 묶여 있다

for key in naver.keys():
    print(key)

print(type(naver.keys()))
to_list = list(naver.keys())
print(to_list)

for key in naver.keys():
    print(key)

for value in naver.values():
    print(value)

for item in naver.items():
    print(item)


# key로 value 찾기
print(naver['name'])
print(naver.get('name'))

# print(naver['passwd'])
# print(naver.get('passwd'))  오류 발생

print(naver.get('passwd' , '앞의 passwd 무시하고 뒤에꺼 출력'))

key = 'passwd'
if naver.get(key) is None :
    print(key + '에 대한 값이 없습니다')

# 'in'
# 'not in' 사용하여 확인

print(key in naver)
print(key not in naver)

if key not in naver:
    print(key + '에 대한 값이 없습니다')
