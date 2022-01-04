# 학생 10명의 점수를 입력 받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하기
scores = [ ]
for i in range(1,11):
    scores.append(int(input('학생 %d 점수를 입력하세요 :'%i)))
total = sum(scores)
average = float(total/len(scores))
print(f'총점은 {total} 입니다.')
print('평균은 %.2f입니다.'%average)

# 강사 코드
scores = []
n = 10
total = 0
for i in range(n):
    score = int(input('점수 입력: '))
    if 0<=score<=100:
        scores.append(score)
    else :
        continue

print(scores)
for score in scores :
    total += score

print('총합은 %d이고, 평균은 %.2f' %(total , total/len(scores)))