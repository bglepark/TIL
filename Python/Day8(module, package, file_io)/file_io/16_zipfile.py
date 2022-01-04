# 파일 압축 및 풀기

import zipfile

# 파일압축
new = zipfile.ZipFile('c:/PythonStudy/Day8/Day8.zip' , 'w')  #경로 지정 , w(write)로 사용
new.write('c:/PythonStudy/Day8/file_io/test2.txt' , compress_type=zipfile.ZIP_DEFLATED) #<- 실제 압축하는 파일을 표시
new.close()

# 압축파일 풀기
ext = zipfile.ZipFile('c:/PythonStudy/Day8/Day8.zip' , 'r') # read 모드로
ext.extractall('c:/PythonStudy/') #extractall 은 모두 다 풀기
ext.close()