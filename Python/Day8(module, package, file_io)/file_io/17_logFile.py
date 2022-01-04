# 로그파일 작성

import os
import datetime, random

if not os.path.isdir('log'):
    os.mkdir('log')

if not os.path.exists('log/countLog.txt'):
    f= open('log/countLog.txt' , 'w', encoding='utf-8')
    f.write('기록시작\n')
    f.close()

# 파일에 로그 기록
with open('log/countLog.txt' , 'a' , encoding='utf-8') as f:
    for _ in range(30): #변수 사용하지 않을거면 _ 사용
        stamp = str(datetime.datetime.now()) #현재 시간
        value = random.random() * 1000000
        log_line = stamp + '\t' + str(value) + '값 생성\n'
        f.write(log_line)
    