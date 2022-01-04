# 화씨 온도를 섭씨 온도로 변환하기

fTemp = 80
cTemp = (fTemp - 32)*5/9

print(cTemp)

print('%f' %cTemp)
# 기본 6자리로 출력

print('%.2f' %cTemp)
print('%6.2f' %cTemp)

print(format(cTemp , '.2f'))

# format() 함수
# format(실수 , '전체 자리수.소수이하자리수<서식기호>')

# 2개 이상의 값 출력
print('화씨 : %d , 섭씨 : %f'  %(fTemp , cTemp))