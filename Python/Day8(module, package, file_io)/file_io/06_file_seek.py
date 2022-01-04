# 파일 내에서 검색
# seek(offset , whence)
# offset(상대위치)
# offset => 시작 위치로부터 열의 위치
# - whence : 위치
# whence => 0: 시작위치 , 1: 현재위치 , 2: 파일의 끝


# seek(0,0) : 시작위치로부터 0열의 위치 => 0행 0열
#  seek(10,0) : 시작위치로부터 오른쪽으로 10열의 이동한 위치 => 0행 10열
# seek(0, 2) : 파일의 끝으로부터 0열의 위치 => 끝행 0열


f = open('test2.txt' , 'r')
f.seek(0,0) #0행 0열
lines = f.readlines()
print(lines)
f.close()

f = open('test2.txt' , 'r')
f.seek(3,0) #0행 4열
lines = f.readlines()
print(lines)
f.close()


# \r : carriage return -> 무조건 1번째 열로 이동한다. (그 다음 첫번째 문자로 간다는 의미)
# \n : line feed 문자 -> 다음 줄로 가게 한다.
f = open('test2.txt' , 'r')
f.seek(10,0) # 한줄마다 \r\n 이 들어가있다.(문자2개)
lines = f.readlines()
print(lines)
f.close()


f = open('test2.txt' , 'r')
f.seek(0,2) # 파일의 마지막 위치
lines = f.readlines()
print(lines)
f.close()


f = open('test2.txt' , 'r')
f.seek(16,0) # 한글은 2바이트씩 잡아먹는다
lines = f.readlines()
print(lines)
f.close()
