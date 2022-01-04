# 1.
# 다음과 같이 이메일주소를 입력받아 이메일 형식인지 아닌지를 판별하여 출력하기

email = input('이메일 입력 : ')
cd_1 = (email.count('@')==1 and email.count('.')==1)
cd_2 = (email.index('@')<email.index('.'))
cd_3 = email.index('@')!=0
cd_4 = (email.index('.')+1)!=len(email)

if cd_1 and cd_2 and cd_3 and cd_4:
    print('이메일 형식이 맞습니다.')
else:
    print('이메일 형식이 아닙니다.')
print("입력한 이메일 : ", email)
