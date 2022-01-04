# 기존 디렉토리 확인

import os.path
os.path.isdir('log') #log 라는 디렉토리가 있는지 확인

# os.mkdir('log')  # 기존에 생성되어 있는 폴더를 또 생성할 때 오류 발생

if not os.path.isdir('log'): #log라는 디렉토리가 없으면 만들어라
    os.mkdir('log')