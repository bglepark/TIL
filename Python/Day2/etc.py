sum1 = 1 + 2 + 3 + 4 +\
      5 + 6 + 7

sum2 = (1+2+3+4+
5+6+7)

#1줄로 인식
print("긴문장으로 표현          "
      " 두번째 "
      "세번째 ")

# 여러 줄로 출력
print("긴문장으로 표현         \n"
      " 두번째 \n"
      "세번째 ")

# escape character
# \n : 줄바꿈
# \t : tab
# \' : '
# \\ : \

print('don\'t')
print('123\t 456')
print("He said ,\"yes\"")
print('He said, "yes"')
print('c:\pythonStudy\name')


print(r'c:\pythonStudy\name')  #r을 사용해서 그대로 사용 (특수문자 의미 제거 :r)

# 2개 명령어(문장) 를 한 줄에 입력
print(sum1) ;print(sum2)

print('apple \n banana \n melon')
print('apple')
print('apple', end=':') # end 인수를 이용해서 줄 안바꾸고 계속 출력
print('banana')


