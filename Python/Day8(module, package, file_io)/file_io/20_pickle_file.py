# 메모리에 로딩된 객체나 정의된 클래스를 파일로 저장하여 사용

import pickle

# 객체 저장 : pickle.dump()
f = open('list.pickle' , 'wb')
result = [1,2,3,4,5]
pickle.dump(result , f) #f에 result를 쓰기
f.close()

# 객체 로딩 : pickle.load()
f = open('list.pickle' , 'rb')
result2 = pickle.load(f)  #f에 있는 정보를 로드함
print(result2)
result2.append(100)
print(result2)
f.close()
