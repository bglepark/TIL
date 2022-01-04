# with 문
# with 문이 종료되면 파일객체는 자동으로 close()
# with open(파일명 , 열기모드) as 파일객체 :
#   수행코드


with open('test3.txt' , 'w') as f : #f=open('test3.txt' , 'w')
    f.write('hello')


# 변수로 지정
file = 'test3.txt'
data = 'hello world!'
with open(file , 'a') as f : #f=open('test3.txt' , 'w')
    f.write('\n'+data)

