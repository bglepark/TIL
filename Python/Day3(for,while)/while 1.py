# while
# 정해진 조건에 따라 반복문 수행


# 초기값
# while 조건 :
#     반복문장1
#     반복문장2
#     ...
#     증감

# 1부터 10까지 출력
for i in range(1,11):
    print(i, end=' ')
print('\n------------------')

i = 1
while i<=10:
    print(i, end=' ')
    i+=1
print()
# 1~10 더하기
i=1
sumN = 0
while i<=10:
    sumN+=1
    i+=1
print(sumN)