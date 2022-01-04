# readline() : 한 줄씩 읽어오기

# 한줄만 읽어오기
# ANSI로 저장되어 있으면 한줄씩 잘 불러옴
f = open('test.txt' , 'r')
line = f.readline()     #  첫번째 라인 1개 읽기 -> 한줄씩 가져와 문자열로 반환
print(line)
f.close()

# 한줄씩 끝까지 읽어오기
f2 = open('test.txt' ,'r')

while True :
    line = f2.readline() #한줄을 읽어오되 코드 뒤에 \n이 붙음
    if not line:
        break
    print(line , end='')

f2.close()