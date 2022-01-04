# 파일 내에서 검색
# read() 함수 사용

f = open('test2.txt' , 'r')
data = f.read()
value = input('검색 값 입력 : ')
if value in data:
    print('Exist!')
else:
    print('No exist!')

f.close()