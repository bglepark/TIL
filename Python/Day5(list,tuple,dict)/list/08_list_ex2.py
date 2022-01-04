# 학생 10명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력,
# 80점 이상의 학생의 수 출력

scores = []
n = 10
total = 0
cnt = 0
for i in range(n):
    score = int(input('점수 입력: '))
    if 0<=score<=100:
        scores.append(score)
    else :
        continue

print(scores)
for score in scores :
    if score>=80 :
        cnt+=1
    total += score

print('총합은 %d이고, 평균은 %.2f' %(total , total/len(scores)))
print('80점 이상 학생 %d명'%cnt)