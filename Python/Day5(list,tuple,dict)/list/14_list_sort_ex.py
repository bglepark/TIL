# 이전 연습문제에서 성적 내림차순으로 정렬

scores = []
n = int(input('학생 수 입력 : '))
total = 0
cnt = 0
i = 1

while True :
    score = input('학생'+str(i)+' 점수 입력 :')
    if score =='':
        break
    scores.append(int(score))
    i +=1

print(scores)
for score in scores :
    if score>=80 :
        cnt+=1
    total += score

print('총합은 %d이고, 평균은 %.2f' %(total , total/len(scores)))
print('80점 이상 학생 %d명'%cnt)
# scores.sort(reverse=True)
sort_scores = sorted(scores , reverse=True)
print(sort_scores)