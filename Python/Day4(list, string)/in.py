# in / not in
# 문자열 내에 특정한 문자열이 포함되어 있는지 확인
# 결과 : True , False

string = 'Python programming'
result = 'on' in string
print(type(result))
print(result)

result_2 = 'on' not in string
print(result_2)

if 'on' in string:
    print("yes")
else :
    print("no")


# 예제. in 활용
ID = input('ID 입력 : ')
ids = ['sun', 'kmlee' , 'moon', 'sky']

if ID in ids :
    print('로그인 성공')
else :
    print('로그인 실패')