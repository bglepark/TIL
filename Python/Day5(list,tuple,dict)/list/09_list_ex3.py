# 학생 n명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력,
# 학생 수 : n
# 80점 이상의 학생의 수 출력

scores = []
n = int(input('학생 수 입력 : '))
total = 0
cnt = 0
for i in range(1 , n+1):
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

# 엔터키를 입력 받을때까지 점수들을 계산

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
