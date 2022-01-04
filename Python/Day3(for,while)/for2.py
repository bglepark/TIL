# for에서 리스트를 이용
# 학생 성적 리스트 score [70,90,100,50,85]
# 60점 이상 합격 , 60점 미만은 불합격 출력
# 1번 학생 합격
# 2번 학생 합격
# 5번 학생 합격
score = [70,90,100,50,85]
number=0
for i in score :
    number = number+1
    if i>=60 :
       print(number,'번째 학생 합격')
    else:
        print(number,'번째 학생 불합격')