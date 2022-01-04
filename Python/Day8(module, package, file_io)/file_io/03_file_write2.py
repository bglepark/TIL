# 파일에 쓰기 : write()

f = open('file4.txt' , 'w' , encoding = 'utf-8')

for i in range(1,11):
    data = '%d행\n' %i
    f.write(data)

f.close()
