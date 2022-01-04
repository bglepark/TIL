# 1 . 이메일 형식인지 판단(강사코드)

# @이 없는 경우
# .이 없는 경우
# @와 . 위치가 바뀐 경우
# @과 . 사이에 문자가 없는 경우
# @ 앞에 문자가 없는 경우
# . 뒤에 문자가 없는 경우
# @ 가 2번 이상 있는 경우
# . 가 2번 이상 있는 경우

#
# email = input('이메일 입력 : ')
# # # -1은 없는 경우를 뜻함
# if email.find('@') == -1 or
#     (email.find('.'))== - 1 or
#     email.index('@') > email.index('.') or
#     email.index(('.')) - email.index('@') < 2 or
#     email.index('@') == 0 or
#     len(email) - email.index('.') <= 1 or
#     email.count('@') >=2 or
#     email.count('.') >=2 :
#     print('이메일 형식이 아니다')
#
# print('입력한 이메일 %s' %email)

