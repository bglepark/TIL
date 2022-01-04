# 2. 텍스트파일로 되어 있는 가사의 단어를 count (yesterday.txt)
# 리스트, 세트 , 딕셔너리 등의 자료구조를 이용
# 단어들은 모두 소문자로 변환하여 사용한다.

f = open('yesterday.txt' , 'r')
yesterday = f.readlines() #리스트로 들어옴
f.close()

words = []
for line in yesterday:
    line = line.split()
    for w in line:
        words.append(w.lower())

wordL = list(set(words))
wordL.sort()  # 알파벳 순으로 정렬

wordDict = dict()
for w in wordL:
    wordDict[w] = words.count(w)         # 전체 리스트에서 count를 사용

for w in wordDict.items():
    print(w)


