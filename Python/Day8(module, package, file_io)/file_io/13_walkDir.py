# 디렉토리 목록 보기

import os

# os.walk('') # 위치를 지정해주면 거기에 대한 하위 목록을 쭉 보여줌

for dirName , subDir , fnames in os.walk('c:/PythonStudy/Day8'):
    print(fnames)
    print('fnames 끝')
    for fname in fnames:
        # print(os.path.join(dirName , fname))
        print(fname)


for dirName , subDir , fnames in os.walk('c:/PythonStudy/Day8'):
    print(dirName)