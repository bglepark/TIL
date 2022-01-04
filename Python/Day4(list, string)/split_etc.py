# 생년월일을 입력하고 연도, 월 , 일을 구분해서 출력
# 생일 입력(연/월/일) : ex) 2000/02/01
# 당신은 2000년에 태어났고
# 생일은 02월 07일 이군요

birth = input('생년월일을 입력하세요(ex_2000/02/01) :')
year = birth.split('/')[0]
month = birth.split('/')[1]
day = birth.split('/')[2]
print('당신의 %s년에 태어났고 , 생일은 %s월 %s일 이군요'%(year,month,day))