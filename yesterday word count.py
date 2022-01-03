# 텍스트파일로 되어 있는 가사의 단어를 count (yesterday.txt)
# 단어들은 모두 소문자로 변환하여 사용한다.
# 모든 단어 개수 count

ly_list = []
fh = open('yesterday.txt' ,'r')
for lyrics in fh:
    lyrics = lyrics.rstrip().lower().replace(',' , ' ').replace('\'' , ' ').split(' ')
    lyrics = list(filter(None, lyrics))
    ly_list.append(lyrics)

ly_list = sum(ly_list,[])


ly_di = {}
for i in range(len(ly_list)):
    count = 0
    for j in range(len(ly_list)):
        if ly_list[i] == ly_list[j]:
            count+=1
    ly_di[ly_list[i]]=count


result1 = list(ly_di.keys())
result2 = list(ly_di.values())


for i in range(len(result1)):
    print('%s : %d ' %(result1[i], result2[i]))


