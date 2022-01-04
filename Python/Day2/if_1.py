# #pw = int(input('비밀번호 입력 :'))
# '''
# if (pw ==1234):
#     print('비밀번호가 일치합니다')
# else :
#     print('비밀번호가 일치하지 않습니다')'''
#
# '''if (pw ==1234):
#     print('비밀번호가 일치합니다')
# else :
#     pass'''
#
# # 문제 : id와 password를 입력받아 두 가지가 다 맞으면 로그인 성공
#
# # id = str(input('id를 입력하세요 : '))
# # pw = int(input('비밀번호를 입력하세요 :'))
# #
# # if (id == 'multicampus') and (pw ==1234) :
# #     print('로그인 성공')
# # else:
# #     print('로그인 실패했습니다.')
# #
#
# # 문제 2 :
# # 정수를 입력받아서 홀수인지 짝수인지 판별하여 출력
#
# number = int(input('정수를 입력하세요 : '))
#
# if number%2 ==0 :
#     print('짝수입니다')
# else :
#     print('홀수입니다')
#
#
# # 입력한 정수가 음수, 0 , 양수 인지를 확인하여 출력
# # 중첩 형식
# if number > 0:
#     print('양수')
# else :
#     if number ==0
#         print('0')
#     else :
#         print('음수')
#
# # 다중 if
# # if~ elif
# if number >0 :
#     print('양수')
# elif number ==0 :
#     print('0')
# else :
#     print('음수')

# 문제 : 점수를 입력 받아서 학점을 출력
score = float(input('성적을 입력하세요 :'))
if score>=90 :
    print('A학점')
elif score>=80 and score<90 :
    print('B학점')
elif score>=70 and score <80 :
    print('C학점')
elif score >=60 and score<70 :
    print('D학점')
else :
    print('F학점')