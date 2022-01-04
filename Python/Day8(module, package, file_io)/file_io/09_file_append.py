# append() : 파일 끝에 추가

f = open('test2.txt' ,'a')  #a : append 모드

appendData = '\n\nPython Programming'
f.write(appendData)

f=open('test2.txt' ,'r')
print(f.read())
f.close()