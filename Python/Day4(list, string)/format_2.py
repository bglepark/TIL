# f'String 사용
# 3.6 이상

tea = 'coffee'
n = 5
s3 = f'나는 {tea}를 좋아해서 하루에 {n}잔 마신다'
print(s3)

# format
# print({0:d}.format(300))

for month in ['1월' , '2월' , '3월']:
    print(f'이번달은 {month}입니다')
    
#  % 서식 문자열 : %s , %d , %f , %c
#string.format()
#1) '문자열 {위치인덱스}'.format(변수)
#2) 문자열{변수}.format{변수==값}
#3) f 포맷