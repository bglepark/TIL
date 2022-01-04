# 문제. 각 학생별 점수 리스트 생성

# 국어 , 영어 , 수학
kim = [90 , 85 , 70]
choi = [88, 92, 70]
kang = [100, 95, 100]
lee = [90 , 60 , 70]

students = [kim , choi , kang , lee]
students_name = ['kim' , 'choi' , 'kang' , 'lee']
subject_name = ['국어' , '영어' , '수학']

# # 학생별 총점과 평균 첨수 출력
# # 과목별 총점과 평균 점수 출력
#
# # print(students)
# #
# # for i in range(len(students)):
# #     print('%s 학생의 총점 : %d점' %  (students_name[i]   ,sum(students[i])))
# #     print('%s 학생의 평균: %.2f점' % (students_name[i] ,(sum(students[i])/len(students[i]))))
# #
#
# # 과목별 총점
# sum_ = 0
# avg_ = 0
# for i in range(len(students)-1):
#     sum_ = 0
#     for j in range(len(students)):
#         sum_ = sum_ + students[j][i]
#         avg_ = sum_/4
#     print('%s의 총점 : %d점 ' % (subject_name[i], students[i][j]))
#     # print('%s의 평균 : %d점 ' % (subject_name[i], avg_))
#
# # "# 각 학생별 점수 리스트 생성
# kim = [90, 85, 70]
# choi = [88, 92, 72]
# kang = [100, 95, 100]
# lee = [90, 60, 70]
#
# students = [kim, choi, kang, lee]
# total = 0
# avg = 0
#
# # 과목별 총점과 평균점수 출력
# for i in range(3):
#     for j in range(4):
#         total += students[j][i]
#     avg = total/4
#     print('%d번째 과목의 합은 %d이고, 평균은 %.2f입니다' %(i+1, total, avg))


# 과목별
kim = [90 , 85 , 70]
choi = [88, 92, 70]
kang = [100, 95, 100]
lee = [90 , 60 , 70]

std_number = len(students)
subject_number = len(students[0])

for i in range(subject_number):
    total = 0
    for j in range(std_number):
        total += students[j][i]

    print('과목%s의 총점은 %d , 평균은 %.2f' %(str(i), total , total/std_number))

# 반올림 하기
round()