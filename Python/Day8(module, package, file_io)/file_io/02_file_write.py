# 파일에 쓰기
# 텍스트 파일에 쓰기 : write()

# data = 'Hi'
# f = open('file2.txt' , 'w')
# f.write(data)    # 파일에 data 쓰기
# f.close()

# data = '안녕하세요'
# f = open('file2.txt' , 'w') # 한글이 ANSI 저장
# f.write(data)    # 파일에 data 쓰기
# f.close()
# # 한글의 경우 UTF-8로 인코딩 해줘야 한다.

data = '안녕하세요'
f = open('file3.txt' , 'w' ,encoding ='utf-8')
f.write(data)    # 파일에 data 쓰기
f.close()