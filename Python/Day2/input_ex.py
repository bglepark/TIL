# 연습문제
# 출력결과


# 국어 점수 입력 : 90
# 영어 점수 입력 : 90
# 수학점수 입력 : 70
# 총점 : 250
# 평균 : 83.33

korea_score = int(input('국어점수 입력 :'))
english_score = int(input('영어점수 입력 :'))
math_score = int(input('수학점수 입력 :'))
result = korea_score+english_score+math_score
print('총정 : %d' %(result))
print('평균: %.2f' %(result/3))

# 연습문제 2
# BMI 지수 계산식 : 몸무게 /(키*키)

# 입력형식
# 몸무게(KG) :
# 키(미터) :

# 출력
# 당신의 BMI는 입니다

weight = float(input('몸무게(KG):'))
height = float(input('키(m):'))

BMI = float(weight / (height*height))
print('당신의 BMI는 %f 입니다'%BMI)
