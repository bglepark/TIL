# readlines() : 전체 라인을 읽어오기 ->  리스트로 가져옴
# 리스트로 반환 : 한 행이 리스트의 요소가 됨

f = open('test.txt' , 'r')
lines = f.readlines()
print(lines) #문자열로 들어감
print(type(lines)) #리스트 형태
f.close()


f = open('test.txt' , 'r')
lines = f.readlines()
for line in lines:
    print(line , end='')
f.close()

f = open('test.txt' , 'r')
for line in f :     #f.readlines() 자동 수행이 된다
    print(line , end='')
f.close()