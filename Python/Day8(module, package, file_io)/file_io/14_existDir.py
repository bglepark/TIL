# 파일 또는 디렉토리 존재 여부 확인 : os.path.exsit()

import os.path

print(os.path.exists('c:/PythonStudy')) # True/False로 나옴
print(os.path.exists('c:/PythonStudy/test.py'))

# 디렉토리인지 파일인지 구분

print(os.path.isdir('c:/PythonStudy'))
print(os.path.isfile('c:/PythonStudy/test.py'))