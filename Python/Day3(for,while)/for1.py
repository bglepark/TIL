# for 변수 in 리스트 또는 범위 :
#   반복문장1
#   반복문장2
# 정해진 횟수만큼 반복

for name in ['apple', 'banana' , 'melon']:
    print(name)

for number in range(10):
    print(number) #0에서 9까지

for number in range(1,10): # 1에서 9까지
    print(number)

# range(시작 , 끝 , 간격)
for number in range(1,10,2):
    print(number)

for number in range(9,0,-2):
    print(number)